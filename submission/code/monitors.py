"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def _late_carriers(trial):
    """Các hãng có kiện trễ (delay > 0) theo sự kiện tracking của trial."""
    for e in trial.get("events") or []:
        if e.get("type") == "tracking":
            return {p.get("carrier_id") for p in e.get("parcels") or [] if (p.get("delay") or 0) > 0}
    return set()


def multi_carrier_late_share(trials):
    """[S6] Tỉ lệ ticket mà đơn có kiện trễ của TỪ HAI HÃNG trở lên (không cần nhãn).
    Đây là nhóm ticket mà 'ai chịu lỗi' không suy ra được từ đơn; tăng lên là dấu hiệu lỗi hãng sắp bị ghi sai."""
    return sum(len(_late_carriers(t)) >= 2 for t in trials) / max(1, len(trials))


def fault_on_non_late_parcel(trials):
    """[S6] Số lệnh ghi lỗi hãng cho một kiện mà tracking ghi là KHÔNG trễ, hoặc cho hãng không có kiện trễ
    (tài xế giao đúng hẹn vẫn bị trừ thưởng). Production phải luôn = 0."""
    bad = 0
    for t in trials:
        delays = {}
        for e in t.get("events") or []:
            if e.get("type") == "tracking":
                delays = {p.get("parcel_id"): (p.get("delay") or 0) for p in e.get("parcels") or []}
        for f in t.get("faults") or []:
            if delays and delays.get(f.get("parcel_id"), 0) <= 0:
                bad += 1
    return bad


def carrier_faults_max_per_day(trials):
    """[S6] Số lỗi tự động nhiều nhất mà MỘT hãng nhận trong một ngày giả lập (theo seed, day).
    Trần đã thống nhất là 2 (ops_limits.max_auto_strikes_per_carrier_per_day); vượt là hãng nhỏ bị 'ghi một lèo'."""
    count = {}
    for t in trials:
        for f in t.get("faults") or []:
            if f.get("ticket_id") == t.get("ticket_id"):
                k = (t.get("seed"), t.get("day"), f.get("carrier_id"))
                count[k] = count.get(k, 0) + 1
    return max(count.values(), default=0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "multi_carrier_late_share": multi_carrier_late_share,
    "fault_on_non_late_parcel": fault_on_non_late_parcel,
    "carrier_faults_max_per_day": carrier_faults_max_per_day,
}
STARTER_MONITORS = ("escalation_rate",)
