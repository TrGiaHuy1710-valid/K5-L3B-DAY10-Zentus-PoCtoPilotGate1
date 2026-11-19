"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Cổng vòng 1 của bàn Zentus (mọi phép so đều dựa trên nguồn sự thật: tracking DB, chính sách theo NGÀY hiệu lực,
bảng phê duyệt, sổ cái; không dựa vào mã ticket hay câu chữ khách viết):
  Cổng 0 · pre_guard          ghim chính sách theo ngày hiệu lực (không tin cờ index_active).
  Cổng 1 · issue_refund       số tiền không vượt quyền lợi tính từ DB; không hoàn khi model fail-open hay khi
                              chữ khách "ra lệnh"; không hoàn lặp; phê duyệt phải hợp lệ; trần hoàn tự động trong ngày.
  Cổng 2 · file_carrier_fault chỉ ghi lỗi khi tracking có nguyên nhân thuộc fault_causes và trễ đủ ngưỡng; ghi đúng kiện trễ;
                              không ghi lặp; quá số lỗi tự động/hãng/ngày thì chuyển người.
  Cổng 3 · notify_carrier     chỉ gửi cho hãng đúng các trường chính sách cho phép (bỏ chữ khách tự gõ, dữ liệu cá nhân).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


# ---------------------------------------------------------------- tra cứu nguồn sự thật
def _policy(ctx):
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _order(ctx, action=None):
    oid = (action or {}).get("order_id") or ctx.ticket.get("order_id")
    return ctx.tools.lookup_order(oid) if oid else None


def _db_view(ctx, order, policy):
    """(kiện trễ nhất, số ngày trễ theo DB, nguyên nhân) — đúng cách agent chọn kiện, nhưng KHÔNG dùng số khách tự khai."""
    parcel = max(order["parcels"], key=lambda p: H.db_delay_days(p, ctx.as_of))
    delay = H.db_delay_days(parcel, ctx.as_of)
    cause = parcel.get("delay_cause") or ("CARRIER" if delay > 0 else None)
    return parcel, delay, cause


def _approval_ok(ctx, approval_id, action):
    if not approval_id:
        return False
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False
    a = rows[0]
    approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
    return (a.get("status") == "valid"
            and a.get("expires_at", "") >= ctx.as_of
            and a.get("order_id") == action.get("order_id")
            and a.get("customer_id") == ctx.ticket.get("customer_id")
            and a.get("max_vnd", 0) >= action.get("amount_vnd", 0)
            and (not approver or a.get("approver_id") == approver))


# ---------------------------------------------------------------- Cổng 0
def pre_guard(ctx):
    pol = _policy(ctx)
    if pol is not None:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


# ---------------------------------------------------------------- Cổng 1–3
def write_gate(ctx, action):
    tool = action.get("tool")
    if tool == "issue_refund":
        return _refund_gate(ctx, action)
    if tool == "file_carrier_fault":
        return _fault_gate(ctx, action)
    if tool == "notify_carrier":
        return _notify_gate(ctx, action)
    return Verdict.allow()


def _refund_gate(ctx, action):
    amount = action.get("amount_vnd", 0) or 0
    # 1a. model không chạy được thì không "hoàn cho vui lòng khách"
    if action.get("basis") != "policy":
        ctx.log("guard_refund", rule="basis_not_policy", basis=action.get("basis"))
        return Verdict.escalate("quyết định hoàn không dựa trên chính sách (model lỗi / fail-open), chuyển người duyệt")
    # 1b. chữ khách viết không được đổi người trả tiền
    if action.get("payer") not in (None, "LOGIX"):
        ctx.log("guard_refund", rule="payer_changed", payer=action.get("payer"))
        return Verdict.escalate("người trả tiền bị đổi theo nội dung ticket, chuyển người duyệt")
    # 1c. không hoàn lặp cho cùng một ticket / đơn
    if ctx.tools.ledger_rows(ticket_id=action.get("ticket_id")) or ctx.tools.ledger_rows(order_id=action.get("order_id")):
        ctx.log("guard_refund", rule="duplicate")
        return Verdict.deny("đơn này đã có dòng hoàn trong sổ cái, không ghi lặp")

    order, policy = _order(ctx, action), _policy(ctx)
    if order is None or policy is None:
        return Verdict.escalate("không tra được đơn hoặc chính sách hiệu lực, chuyển người duyệt")
    if order.get("customer_id") != ctx.ticket.get("customer_id"):
        ctx.log("guard_refund", rule="customer_mismatch")
        return Verdict.escalate("người yêu cầu không phải chủ đơn, chuyển người duyệt")

    # 1d. số tiền không vượt quyền lợi tính từ tracking DB (không dùng số ngày khách tự khai)
    _, delay, cause = _db_view(ctx, order, policy)
    entitled = H.entitlement_vnd(policy, order, delay, cause)
    if entitled <= 0:
        ctx.log("guard_refund", rule="not_entitled", db_delay=delay, cause=cause, asked=amount)
        return Verdict.deny(f"theo tracking DB trễ {delay} ngày, chưa đủ điều kiện hoàn")
    if amount > entitled:
        ctx.log("guard_refund", rule="cap_to_entitlement", db_delay=delay, asked=amount, entitled=entitled)
        action = dict(action, amount_vnd=entitled)
        amount = entitled
        verdict = Verdict.modify(f"hạ số tiền về quyền lợi theo DB ({entitled}đ)", amount_vnd=entitled)
    else:
        verdict = Verdict.allow()

    # 1e. vượt hạn mức tự động thì phải có phê duyệt hợp lệ
    if amount > policy["auto_limit_vnd"] and not _approval_ok(ctx, action.get("approval_id"), action):
        ctx.log("guard_refund", rule="approval_invalid", approval_id=action.get("approval_id"))
        return Verdict.escalate("vượt hạn mức tự động mà phê duyệt không hợp lệ, chuyển người duyệt")

    # 1f. trần tiền tự động trong ngày: trần của bàn (config); chưa đặt thì dùng ngân sách Finance (ops_limits)
    lim = ctx.tools.ops_limits() or {}
    cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd") \
        or lim.get("daily_auto_refund_budget_vnd")
    if cap is not None and not action.get("approval_id") and ctx.tools.auto_refund_today_vnd() + amount > cap:
        ctx.log("guard_refund", rule="daily_cap", cap=cap)
        return Verdict.escalate("vượt trần hoàn tự động trong ngày, chuyển người duyệt")
    return verdict


def _fault_gate(ctx, action):
    order, policy = _order(ctx, action), _policy(ctx)
    if order is None or policy is None:
        return Verdict.deny("không tra được đơn hoặc chính sách, không ghi lỗi hãng")
    # 2a. không ghi lặp
    if ctx.tools.fault_rows(ticket_id=action.get("ticket_id")) or ctx.tools.fault_rows(order_id=action.get("order_id")):
        ctx.log("guard_fault", rule="duplicate")
        return Verdict.deny("đơn này đã có lỗi hãng, không ghi lặp")
    # 2b. ghi đúng kiện trễ theo DB và chỉ khi nguyên nhân ghi nhận thuộc lỗi hãng
    parcel, delay, _ = _db_view(ctx, order, policy)
    if not H.carrier_at_fault(policy, parcel, delay):
        ctx.log("guard_fault", rule="not_at_fault", parcel_id=parcel["parcel_id"], db_delay=delay,
                cause=parcel.get("delay_cause"))
        return Verdict.deny("tracking không ghi nhận lỗi hãng đủ điều kiện, không ghi lỗi")
    # 2c. trần số lỗi tự động cho một hãng trong ngày
    max_strikes = (ctx.tools.ops_limits() or {}).get("max_auto_strikes_per_carrier_per_day")
    if max_strikes is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= max_strikes:
        ctx.log("guard_fault", rule="strike_cap", carrier_id=parcel["carrier_id"])
        return Verdict.escalate(f"hãng {parcel['carrier_id']} đã đủ {max_strikes} lỗi tự động hôm nay, chuyển người duyệt")
    changes = {}
    if action.get("parcel_id") != parcel["parcel_id"]:
        changes.update(parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"))
    if action.get("delay_days") != delay:
        changes["delay_days"] = delay
    if changes:
        ctx.log("guard_fault", rule="fix_parcel_or_delay", **{k: v for k, v in changes.items() if k != "driver_id"})
        return Verdict.modify("ghi lỗi theo kiện và số ngày trễ trong tracking DB", **changes)
    return Verdict.allow()


def _notify_gate(ctx, action):
    policy = _policy(ctx)
    allowed = set(policy["carrier_notice_fields"]) if policy else {"order_id", "parcel_id", "district", "delay_days"}
    blocked = set((ctx.gates or {}).get("legal", {}).get("pii_fields_blocked_to_third_party") or [])
    payload = action.get("payload") or {}
    clean = {k: v for k, v in payload.items() if k in allowed and k not in blocked}
    if clean != payload:
        ctx.log("guard_notify", rule="strip_fields", removed=sorted(set(payload) - set(clean)))
        return Verdict.modify("chỉ gửi hãng các trường chính sách cho phép", payload=clean)
    return Verdict.allow()
