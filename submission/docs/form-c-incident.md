# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3B-DAY10-Zentus-PoCtoPilotGate1 · **Thẻ đã bốc:** S6 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | R-S6-prepared-20261119-161231-2b41c3 (grade `R-S6-grade-20261119-161230-2b41c3`) | S6 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 0.6667 [0.4167; 0.9167] | 0.6667 | 270000 · 10 · 0 | 0.1667 | Cổng vòng 1 đã sửa đúng kiện cho đơn tách kiện (lỗi oan 40 → 10), nhưng đơn có hai hãng cùng trễ mà khách không chỉ rõ kiện (S6-20, S6-21) vẫn bị hoàn tiền và ghi lỗi cho một hãng; ROI 0.14 < 0.3. |
| 2 | R-S6-after-20261119-161356-e2825f | S6 · after | Nhiều hãng cùng trễ + ticket không chỉ rõ kiện → chuyển người TRƯỚC lệnh hoàn; quá trần 2 lỗi/hãng/ngày → bỏ riêng lệnh ghi lỗi (không escalate sau khi đã hoàn); ghi lỗi theo kiện khách chỉ rõ; thêm 3 monitor | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.1667 | Đủ mọi ngưỡng đã ký trên gói thẻ; ROI 1.08. |
| 3 | R-S6-after-20261119-161405-e2825f (grade `R-S6-grade-20261119-161404-e2825f`) | S6 · after | (không đổi code; lệnh tự kiểm tra ba mốc) | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.1667 | visible ✅, regression ✅, monitor ✅; còn integrity ❌ do kiểu xuống dòng CRLF của Git trên máy (không phải sửa file khoá). |
| 4 | R-base-after-20261119-161357-e2825f | base · after | (kiểm không regression) | 1.0 [1.0; 1.0] | 1.0 | 0 · 0 · 0 | 0.2273 | Bộ nền vẫn 110/110; không ca nào hỏng thêm; `Ran 13 tests … OK`. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S6-grade-20261119-161230-2b41c3` · base: `R-S6-before-20261119-161231-2b41c3` · prepared: `R-S6-prepared-20261119-161231-2b41c3`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): lỗi hãng oan **40 → 10** (Cổng 2 sửa lệnh ghi lỗi từ "kiện đầu tiên" về kiện trễ theo DB, và từ chối ghi khi kiện không đủ ngưỡng); pass_rate **0.3333 → 0.6667**; hãng GHSH oan 30 → 5, DNB 10 → 5; kho HN về 1.0. **Chưa đỡ được**: tiền hoàn sai vẫn **270.000đ** (S6-20, S6-21), 10 lỗi oan còn lại.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: **ROI 0.14 < 0.3** (prepared). Ở mốc prepared, tỉ lệ chuyển người tăng 0 → 0.1667 và chi phí 3.162 → 4.828đ/ticket, vì Cổng 2 escalate ở lỗi thứ 3 của một hãng **sau khi tiền đã hoàn** (S6-42, S6-43): vừa tốn công người vừa không đúng nhãn.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? **Kỹ thuật** (mô hình dữ liệu "một đơn = một hãng") và **pháp lý / con người** (bên thứ ba là hãng nhỏ và tài xế bị trừ thưởng chuyên cần, không được hỏi).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Một phần.** HAZOP B4 có dòng INCOMPLETE "đơn nhiều kiện ghi lỗi theo kiện đầu tiên", nên Cổng 2 đã sửa về kiện trễ nhất: đỡ được 30/40 lỗi oan. Bàn **không nghĩ tới** trường hợp **hai hãng cùng trễ mà khách không nói kiện nào**: bàn ngầm cho rằng "kiện trễ nhất" luôn là kiện có lỗi, tức vẫn đoán thay vì dừng. Bàn cũng đặt trần 2 lỗi/hãng/ngày nhưng cho escalate **sau** khi tiền đã ghi.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Đơn có hai hãng cùng trễ, khách không nói kiện nào, trợ lý vẫn tự chọn một hãng để ghi lỗi; hãng nhỏ bị trừ thưởng, Sông Hồng ngừng hợp tác | Pháp lý / con người | Trace `tracking.parcels` có ≥ 2 hãng trễ đủ ngưỡng, ticket không có `parcel_id` (S6-20, S6-21); monitor `multi_carrier_late_share` |
| Một hãng nhận "một lèo" nhiều lỗi trong ngày, vượt trần 2 lỗi đã thống nhất với Ops | Con người và vận hành | `ops_limits.max_auto_strikes_per_carrier_per_day = 2`; monitor `carrier_faults_max_per_day` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `hãng vận chuyển nhỏ (Sông Hồng) và tài xế của hãng bị trừ thưởng chuyên cần; LogiX hoàn tiền cho ca chưa xác định được` · đo bằng gì `wrongful_carrier_faults (số lệnh ghi lỗi oan) và wrongful_refund_vnd` · bao nhiêu ở mốc base `40 lỗi oan · 270.000đ hoàn sai (R-S6-before-20261119-161231-2b41c3)`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S6-01@11` mốc base: `tracking parcels [{O-2601-P1, GHSH, delay 0}, {O-2601-P2, VNX, delay 4}]` nhưng lệnh ghi lỗi dùng `parcels[0]` (agent: "order-level carrier = carrier of the first parcel") → LỖI HÃNG cho **GHSH / O-2601-P1** là kiện giao đúng hẹn; monitor `fault_on_non_late_parcel` = 15 ở base | Tài xế GHSH bị trừ thưởng dù giao đúng hẹn; VNX (hãng thật sự trễ) thoát; khách không thấy gì sai | cao | **lỗi chìm** |
| 2 | `S6-21@11` mốc prepared: `tracking parcels [{O-2621-P1, DNB, 4}, {O-2621-P2, MKD, 4}]`, ticket không có `parcel_id` ("Mỹ phẩm về muộn, đề nghị hoàn phí") → `issue_refund 28000` → `file_carrier_fault O-2621-P1 DNB`. Nhãn: `escalated`, không hoàn, không lỗi. Tương tự `S6-20@11` (GHSH trễ 3, VNX trễ 5 → hệ thống ghi VNX) | DNB bị ghi lỗi trong khi MKD cũng trễ y hệt; LogiX hoàn 28.000đ khi chưa rõ ai chịu; chị Oanh không có căn cứ đòi tiền hãng | cao | **lỗi chìm** (hệ thống "tự tin" chọn một hãng; không ai được báo là có mơ hồ) |
| 3 | `S6-42@11` mốc prepared: `guard_fault rule strike_cap carrier GHSH` → `gate escalate` sau khi `issue_refund 22000` đã ghi; kết quả `status escalated` nhưng SỔ CÁI đã có 22.000đ. Nhãn: `refunded`, không lỗi hãng | Khách nhận "đang chờ duyệt" dù đã được hoàn; chị Hạnh nhận thêm một ca vô ích; chi phí mỗi ticket tăng (ROI 0.74 → 0.14) | thấp | **lỗi ngữ cảnh** (hệ thống "chạy đúng thiết kế" của cổng, nhưng người dùng thấy trạng thái trái với thực tế) |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | ✘ | ✔ Khách nói "đơn giao chậm" (cả đơn), hệ thống tự diễn giải thành "kiện trễ nhất / kiện đầu tiên là kiện có lỗi" | ✘ |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | ✔ Agent chỉ đọc hãng của `parcels[0]`, bỏ qua dữ liệu từng kiện dù có sẵn | ✔ Thiếu `parcel_id` trong ticket: không đủ thông tin để biết hãng nào chịu | ✘ |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | ✘ | ✘ | ✔ Cổng trần lỗi (đòi người duyệt) và agent (đã ghi tiền) cùng quyết trạng thái ticket; thứ tự "tiền trước, lỗi sau" làm escalate muộn |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | ✘ | ✘ | ✔ Một ngày nhiều đơn của cùng hãng → mọi ticket từ lỗi thứ 3 đều rơi vào trạng thái lệch |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Điều phối hãng xác định lỗi theo **kiện** và quét giao của tài xế: kiện của GHSH giao đúng hẹn thì GHSH không có lỗi | Kế toán đối soát cần bằng chứng kiện nào trễ, do hãng nào, nguyên nhân gì; "không rõ kiện" thì không ghi được | Khách thấy "chờ duyệt" mà tiền đã về; người duyệt nhận ca không có gì để duyệt |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | **Khác: cổng code sửa tham số** (ghi lỗi đúng kiện, đúng hãng, đúng tài xế theo tracking) | **Trao quyền kiểm soát cho người**: chuyển người duyệt TRƯỚC lệnh hoàn, không đoán | **Khác: đổi hành động của cổng** từ escalate sang bỏ riêng lệnh ghi lỗi (tiền giữ nguyên, lỗi thứ 3+ để người duyệt ghi tay) |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Ticket → hoàn đúng → lỗi ghi cho VNX / O-2601-P2 (kiện trễ) → chị Oanh đối soát khớp | Ticket → cổng thấy ≥ 2 hãng cùng trễ, không có `parcel_id` → chuyển chị Hạnh → hỏi khách / đối chiếu tracking → duyệt hoàn và ghi lỗi tay cho đúng hãng | Ticket → hoàn → không ghi lỗi tự động (đã đủ 2) → khách nhận "đã hoàn" → cuối ngày chị Hạnh xem dấu `strike_cap` trong trace và quyết có ghi lỗi tay không |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `fault_on_non_late_parcel` | `multi_carrier_late_share` | `carrier_faults_max_per_day` |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `Điều phối / trưởng nhóm tài xế của hãng (ví dụ Sông Hồng, GHSH, VNX)` | Nhóm B: `Kế toán đối soát hãng và shop (chị Oanh, NV-OANH)` |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | Nhận thông báo `notify_carrier` và lỗi `file_carrier_fault` ghi cho hãng / tài xế (`driver_id`); lỗi tính vào thưởng chuyên cần của tài xế | Dùng sổ cái hoàn tiền và sổ lỗi hãng để đối soát hằng tuần, đòi lại tiền từ hãng chịu lỗi |
| Mục tiêu chính của họ | Chỉ nhận lỗi cho kiện chính hãng mình chở và giao trễ; bảo vệ thưởng của tài xế | Mỗi khoản hoàn và mỗi lỗi hãng khớp với tracking từng kiện, có căn cứ để thu hồi |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | (1) Tra mã kiện trong lịch sử quét của tài xế; (2) so ngày giao thực tế với ngày hẹn **của kiện đó**; (3) xem nguyên nhân trễ (lỗi hãng / bất khả kháng / khách vắng); (4) chỉ nhận lỗi khi cả ba khớp | (1) Lấy dòng hoàn trong sổ cái; (2) xác định kiện bị khiếu nại; (3) đối chiếu tracking từng kiện và `delay_cause`; (4) đơn tách kiện mà nhiều hãng cùng trễ → hỏi CSKH / khách kiện nào bị khiếu nại, hoặc chia theo quy định trước khi ghi |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Khá đồng đều trong một hãng (theo quét kiện), nhưng mỗi hãng có quy định thưởng / phạt riêng | Đồng đều cho đơn một kiện; với đơn tách kiện nhiều hãng thì **chưa có quy định chung**, mỗi người xử lý một kiểu |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | **Kiện** (và tài xế chở kiện đó) | **Kiện** (gắn với hãng chở kiện); tiền hoàn tính theo đơn nhưng lỗi tính theo kiện |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `ĐƠN HÀNG (một đơn = một hãng = hãng của kiện đầu tiên)`. Bằng chứng: ticket `S6-01@seed 11` (mốc base), dòng trace: `tracking parcels [{O-2601-P1, GHSH, delay 0}, {O-2601-P2, VNX, delay 4}]` nhưng `file_carrier_fault parcel_id O-2601-P1, carrier_id GHSH` (code agent: "order-level carrier = carrier of the first parcel").
- Chỗ hai hình dung vênh nhau: `Người chịu hậu quả xét lỗi theo KIỆN; hệ thống xét theo ĐƠN và lấy kiện đầu tiên, nên kiện giao đúng hẹn của hãng A gánh lỗi cho kiện trễ của hãng B. Cổng vòng 1 đổi sang "kiện trễ nhất", vẫn là một phép ĐOÁN khi nhiều hãng cùng trễ (S6-20@11: GHSH trễ 3, VNX trễ 5 → ghi VNX; S6-21@11: DNB và MKD cùng trễ 4 → ghi DNB).`
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `tự chọn một hãng (kiện đầu tiên ở base, kiện trễ nhất ở prepared), hoàn tiền và ghi lỗi luôn`; nên làm gì: `không đoán: dừng TRƯỚC lệnh ghi đầu tiên (issue_refund), chuyển người duyệt (NV-HANH) để xác định kiện; không tự ghi lỗi hãng. Khi khách chỉ rõ parcel_id thì ghi đúng kiện đó.`

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault`

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `carrier_id` / `parcel_id` / `driver_id` | WRONG | Agent lấy hãng của `parcels[0]` cho cả đơn: `S6-01` ghi GHSH / O-2601-P1 (giao đúng hẹn) thay vì VNX / O-2601-P2 (trễ 4 ngày) | Tài xế GHSH bị trừ thưởng; VNX thoát lỗi; đối soát sai | Cổng 2 vòng 1 (`modify` về kiện trễ theo DB) | **Chặn / sửa**: giữ Cổng 2; vòng 2 ưu tiên kiện khách chỉ rõ (`ticket.parcel_id` qua `H.ticket_parcel`) |
| Ticket không có `parcel_id`, đơn có ≥ 2 hãng cùng trễ đủ ngưỡng | INCOMPLETE | `S6-20` (GHSH trễ 3, VNX trễ 5), `S6-21` (DNB và MKD cùng trễ 4): không đủ thông tin để biết kiện bị khiếu nại; cổng vòng 1 vẫn chọn "kiện trễ nhất" | Một hãng bị ghi lỗi oan; LogiX hoàn 26.000–28.000đ khi chưa xác định ai chịu (270.000đ trên 5 seed) | Không (cổng vòng 1 vẫn đoán) | **Chặn**: `_refund_gate` escalate TRƯỚC lệnh hoàn khi `len(_late_carriers) ≥ 2` và ticket không có `parcel_id`; `_fault_gate` deny cùng điều kiện (lớp thứ hai) |
| Số lỗi đã ghi cho một hãng trong ngày | INCAPABLE (hãng nhỏ không chịu nổi) | `S6-40`…`S6-43`: bốn đơn GHSH cùng ngày; base ghi 4 lỗi một lèo (monitor `carrier_faults_max_per_day` = 4); prepared escalate lỗi thứ 3 **sau khi tiền đã hoàn** | Hãng nhỏ bị ghi dồn lỗi; ticket rơi vào trạng thái lệch (đã hoàn mà vẫn chờ duyệt) | Cổng 2 vòng 1 (escalate ở trần 2) | **Giới hạn thiệt hại**: ở trần 2 lỗi/hãng/ngày thì `deny` riêng lệnh ghi lỗi, tiền giữ nguyên; người duyệt xem dấu `strike_cap` và ghi tay nếu đúng |
| `delay_cause` của từng kiện khi một kiện bất khả kháng, kiện kia lỗi hãng | WRONG | *(Nhánh bàn chưa thấy trên trace.)* Đơn tách kiện: kiện A trễ do `FORCE_MAJEURE`, kiện B trễ do `CARRIER`, khách không nói kiện nào. Hệ thống có thể lấy nguyên nhân của kiện trễ nhất (A) rồi ghi lỗi cho hãng của B, hoặc ngược lại. Từ 01/12 (REFUND-v4), bất khả kháng không còn trong `fault_causes` | Hãng bị ghi lỗi cho ca bão; hoặc hãng có lỗi thật thoát | Cổng 2 kiểm `carrier_at_fault` trên **chính kiện được ghi** | **Chặn**: giữ nguyên tắc nguyên nhân và kiện phải là của cùng một kiện; nhiều hãng cùng trễ → chuyển người (cổng vòng 2) |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: **Mỗi lệnh `file_carrier_fault` phải trỏ tới đúng một kiện mà tracking DB ghi là trễ ≥ `min_days_fee` với `delay_cause` thuộc `fault_causes` của chính sách hiệu lực, và `carrier_id` / `driver_id` phải là của chính kiện đó. Nếu ticket không chỉ rõ kiện mà có từ hai hãng cùng trễ đủ ngưỡng, hệ thống không được ghi tiền hay lỗi tự động (phải chuyển người).**

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): `_fault_gate` (kiểm `H.carrier_at_fault` trên kiện từ `H.ticket_parcel`, `modify` carrier / driver theo kiện), `_refund_gate` nhánh `ambiguous_multi_carrier`; report: `wrongful_carrier_faults = 0`, `wrongful_refund_vnd = 0`; monitor `fault_on_non_late_parcel = 0`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): **"Một đơn hàng do một hãng chở trọn vẹn", và khi khách khiếu nại "đơn giao chậm" thì luôn xác định được kiện nào, hãng nào có lỗi.**

Vì sao có thể sai: Ngoài thực tế LogiX tách đơn theo kho và theo năng lực hãng (đơn nhiều món, hàng cồng kềnh, hàng từ nhiều shop), nên một đơn có nhiều kiện do nhiều hãng chở. Khách chỉ thấy "đơn của tôi" và hiếm khi biết mã kiện. Vào mùa cao điểm hoặc sau bão, nhiều kiện của cùng đơn cùng trễ. Thêm nữa, tracking từng kiện do từng hãng tự cập nhật, nên có thể lệch nhau về giờ quét.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S6-prepared-20261119-161231-2b41c3` · base `R-S6-before-20261119-161231-2b41c3`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: tài xế hãng nhỏ bị trừ thưởng vì lỗi giao trễ ghi oan (cho ai: hãng vận chuyển + tài xế; LogiX mất tiền hoàn sai, đo bằng: wrongful_carrier_faults = 40 ở base, 10 ở prepared; wrongful_refund_vnd = 270.000đ)
 └─ HOẶC
 ├─ [1] Lỗi ghi cho kiện giao ĐÚNG hẹn của hãng khác trong đơn tách kiện   tầng: hành động (tool)
 │ └─ vì: agent lấy hãng của parcels[0] cho cả đơn (mô hình "một đơn = một hãng")   bằng chứng: ticket S6-01@seed 11 (base): ghi GHSH/O-2601-P1 delay 0; monitor fault_on_non_late_parcel = 15
 ├─ [2] Nhiều hãng cùng trễ, khách không chỉ rõ kiện, hệ thống vẫn tự chọn một hãng và hoàn tiền   tầng: đầu vào / quyền hạn
 │ └─ vì: thiếu parcel_id trong ticket VÀ không có quy tắc "không đủ thông tin thì dừng"   bằng chứng: ticket S6-21@seed 11 (prepared): DNB và MKD cùng trễ 4 → ghi DNB; S6-20@11: GHSH 3, VNX 5 → ghi VNX
 └─ [3] Một hãng bị ghi dồn nhiều lỗi trong một ngày ("một lèo")   tầng: vận hành / kinh doanh
   └─ vì: không có trần số lỗi tự động mỗi hãng mỗi ngày ở base; ở prepared trần có nhưng escalate SAU khi đã hoàn tiền   bằng chứng: S6-40…S6-43 cùng GHSH; monitor carrier_faults_max_per_day = 4 (base); S6-42@11 status escalated mà sổ cái đã có 22.000đ; ROI prepared 0.14 < 0.3
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Lỗi hãng phải ghi cho đúng kiện trễ theo tracking, với `carrier_id` / `driver_id` của chính kiện đó | "Một đơn chỉ do một hãng chở" |
| [2] | Khi không xác định được kiện (≥ 2 hãng cùng trễ, không có `parcel_id`), không được tự ghi tiền hay lỗi; phải chuyển người trước lệnh ghi đầu tiên | "Khách luôn nói rõ kiện nào bị trễ" / "kiện trễ nhất là kiện bị khiếu nại" |
| [3] | Không quá `max_auto_strikes_per_carrier_per_day = 2` lỗi tự động cho một hãng mỗi ngày; cổng không được để ticket ở trạng thái lệch (đã hoàn mà vẫn chờ duyệt) | "Lỗi của một hãng rải đều theo ngày" / "hãng nhỏ chịu được nhiều lỗi dồn một lúc" |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Agent ghi lỗi theo `parcels[0]` | `_fault_gate`: kiện = `H.ticket_parcel(order, ticket)` (kiện khách chỉ rõ, không thì kiện trễ nhất theo DB); `carrier_at_fault` trên chính kiện đó; `modify` `parcel_id` / `carrier_id` / `driver_id` / `delay_days`. Cổng vòng 1 đã có phần "kiện trễ nhất"; vòng 2 thêm ưu tiên `ticket.parcel_id` | chặn | **NGĂN** với dữ liệu tracking đúng: cổng không đọc lựa chọn của agent mà tính lại kiện từ DB rồi ghi đè tham số; mọi lệnh ghi lỗi đều đi qua `write_gate` | R-S6-after-20261119-161356-e2825f |
| [2] | Không đủ thông tin (≥ 2 hãng trễ, không có `parcel_id`) mà vẫn đoán | `_refund_gate` nhánh `ambiguous_multi_carrier` → `Verdict.escalate` TRƯỚC `issue_refund`; `_fault_gate` cùng điều kiện → `deny` (lớp thứ hai); hàm `_late_carriers` | chặn (trả quyền cho người duyệt NV-HANH) | **NGĂN** hệ thống tự ghi trong nhóm ca này (dừng trước lệnh ghi đầu tiên); nhưng chỉ **GIẢM** tác hại chung, vì người duyệt vẫn có thể quyết sai, và nếu khách ghi sai `parcel_id` thì cổng tin `parcel_id` đó | R-S6-after-20261119-161356-e2825f |
| [3] | Ghi dồn lỗi cho một hãng; escalate sau khi đã hoàn | `_fault_gate` nhánh `strike_cap`: đổi `escalate` → `deny` riêng lệnh ghi lỗi (tiền giữ nguyên), ghi dấu `strike_cap` vào trace; trần lấy từ `ops_limits.max_auto_strikes_per_carrier_per_day = 2` | giới hạn thiệt hại | **GIẢM**: hãng nhận tối đa 2 lỗi tự động mỗi ngày (monitor 4 → 2), lỗi thứ 3+ cần người ghi tay; nhưng 2 lỗi đầu vẫn có thể sai nếu tracking sai | R-S6-after-20261119-161356-e2825f |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `fault_on_non_late_parcel` (chính) · kèm `multi_carrier_late_share`, `carrier_faults_max_per_day` |
| **Bước / hành vi được đo** | Bước ghi lỗi hãng (`file_carrier_fault`) trên đơn tách kiện |
| **Thước đo** (một câu, có đơn vị) | Số lệnh ghi lỗi hãng cho một kiện mà tracking ghi là **không trễ** (lệnh / ngày). Kèm: tỉ lệ ticket có kiện trễ của ≥ 2 hãng (%), và số lỗi tự động nhiều nhất một hãng nhận trong một ngày (lỗi / hãng / ngày) |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `events` (sự kiện `tracking.parcels[].parcel_id, carrier_id, delay`), `faults` (các dòng `file_carrier_fault`: `parcel_id`, `carrier_id`, `ticket_id`), `seed`, `day` |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `fault_on_non_late_parcel` = Σ số dòng `faults` mà `delay` của `parcel_id` đó trong `tracking` ≤ 0 (trial không có sự kiện `tracking` thì bỏ qua). `multi_carrier_late_share` = số trial có ≥ 2 `carrier_id` khác nhau với `delay > 0` / tổng trial. `carrier_faults_max_per_day` = max theo (seed, day, carrier) của số lỗi ghi trong trial đó |
| **Khung thời gian / ngưỡng báo động** | Theo ngày vận hành. `fault_on_non_late_parcel` **≥ 1 → ĐỎ**: tắt `file_carrier_fault` (NV-TUNG, 15 phút). `carrier_faults_max_per_day` > 2 → ĐỎ (trần Ops bị vượt); = 2 → VÀNG, NV-OANH báo hãng. `multi_carrier_late_share` > 0,2 → VÀNG: lượng ca chuyển người sẽ tăng, xem số người trực |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy lỗi ghi cho kiện **có trễ** nhưng sai hãng chịu (khi tracking ghi sai nguyên nhân, hoặc khách ghi sai `parcel_id`); không thấy lỗi bị bỏ sót (hãng có lỗi mà không bị ghi) |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | `fault_on_non_late_parcel`: bộ nền 0 · thẻ base **15**, after 0. `multi_carrier_late_share`: bộ nền 0 · thẻ **0,25**. `carrier_faults_max_per_day`: bộ nền 1 · thẻ base **4**, after **2** (report grade `R-S6-grade-20261119-161404-e2825f`, monitor ✅) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S6-after-20261119-161405-e2825f`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Tài xế hãng nhỏ bị trừ thưởng vì lỗi giao trễ ghi oan (after: wrongful_carrier_faults = 0, wrongful_refund_vnd = 0)
 └─ HOẶC
 ├─ [1] Agent ghi lỗi cho kiện đầu tiên / kiện không trễ VÀ [gate _fault_gate (kiện theo DB, carrier_at_fault, modify) hỏng]
 ├─ [2] Nhiều hãng cùng trễ, không rõ kiện VÀ [gate _refund_gate ambiguous_multi_carrier hỏng] VÀ [gate _fault_gate ambiguous_multi_carrier hỏng]
 └─ [3] Một hãng bị ghi dồn lỗi VÀ [gate strike_cap hỏng]   (còn hở: 2 lỗi đầu mỗi ngày vẫn tự động; tracking sai; khách ghi sai parcel_id)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `_fault_gate` (`H.ticket_parcel`, `H.carrier_at_fault`, `modify`) + `legal.carrier_fault_requires_recorded_cause = true` + metric `fault_on_non_late_parcel` | chặn + phát hiện | **Ngăn** khi tracking đúng: cổng tính lại kiện và nguyên nhân từ DB, không dựa vào lựa chọn của agent | Tracking DB của hãng ghi sai ngày giao / nguyên nhân |
| [2] | `_refund_gate` + `_fault_gate` nhánh `ambiguous_multi_carrier`; metric `multi_carrier_late_share` | chặn (trả quyền cho người) | **Ngăn** hệ thống tự ghi trong ca mơ hồ (hai lớp cổng); chỉ **giảm** tác hại vì quyết định chuyển sang người | Khách ghi sai `parcel_id`; người duyệt quá tải rồi duyệt nhanh; cùng một hãng có hai kiện trễ (không mơ hồ về hãng nhưng mơ hồ về kiện, cổng vẫn cho qua) |
| [3] | `_fault_gate` nhánh `strike_cap` (`ops_limits.max_auto_strikes_per_carrier_per_day = 2`) + metric `carrier_faults_max_per_day` | giới hạn thiệt hại | **Giảm**: trần số lỗi, không chặn lỗi sai trong 2 lỗi đầu | Trần tính trên sổ lỗi trong ngày giả lập; nếu sổ lỗi bị reset hoặc nhiều tiến trình ghi song song thì trần có thể bị vượt |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Đơn tách kiện nhiều hãng tăng (mùa sale, đơn nhiều shop) làm lượng ca "không rõ kiện" chuyển người tăng, hàng chờ của chị Hạnh vượt SLA 60 phút | Trung bình | Cao (ca ùn, chi phí vượt 7.000đ/ticket, ROI giảm) | Trần Thị Hạnh (NV-HANH) | `multi_carrier_late_share` > 0,2 hoặc `escalation_rate` > 0,25; report "số ca bị ùn" ≥ 1 | Thêm người trực giờ cao điểm (B7.6); đề nghị app CSKH bắt khách chọn kiện khi khiếu nại đơn tách kiện (giảm ca mơ hồ từ gốc) | Nếu vượt ngưỡng trong pilot: Thu hẹp (loại đơn tách kiện nhiều hãng khỏi phạm vi tự động) | MANAGE |
| Một hãng vẫn bị ghi lỗi sai vì tracking của hãng đó ghi sai `delivered_date` / `delay_cause` (cổng tin tracking) | Thấp | Cao (bên thứ ba bị phạt oan, quan hệ đối tác) | Phạm Kiều Oanh (NV-OANH) | Số khiếu nại lỗi từ hãng mỗi tuần ≥ 1; `fault_on_non_late_parcel` ≥ 1 | Đối soát tuần với hãng; khiếu nại hợp lệ → huỷ lỗi, đưa ca vào bộ thử | Bước đánh giá 2 phải có số khiếu nại thật từ hãng | MEASURE |
| Trần 300.000đ / khách / ngày chưa có cổng (sổ cái không tách được dòng của hôm nay) | Thấp | Trung bình (một khách nhận nhiều khoản tự động) | Lê Thanh Tùng (NV-TUNG) | Tổng hoàn tự động một khách / ngày > 300.000đ (cần thêm metric) | Thêm cổng khi host có ngày cho từng dòng sổ cái; trước đó NV-OANH kiểm cuối ngày | Không chặn Gate 1; phải xong trước Bước đánh giá 2 | GOVERN |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 Chất lượng | Xong (bộ nền + gói S6) · Chưa (test ẩn) | `R-S6-after-20261119-161405-e2825f`: pass_rate 1.0, pass_k 1.0; `R-base-after-20261119-161357-e2825f`: 110/110; C2 | Lê Thanh Tùng (NV-TUNG) |
| 2 Dữ liệu | Xong | C3.2: đơn vị chịu lỗi là **kiện**, không phải đơn; cổng đọc `parcels[]` từng kiện | Lê Thanh Tùng (NV-TUNG) |
| 7 Vận hành | Xong | 3 metric mới trong `lab10/monitors.py` (monitor ✅); Runbook 4–5 dưới đây | Lê Thanh Tùng (NV-TUNG) |
| 8 Con người, pháp lý | Xong (cổng) · Chưa (quy trình huỷ lỗi oan với hãng) | Lỗi hãng oan 40 → 0; trần 2 lỗi/hãng/ngày; NV-OANH nhận khiếu nại hãng | Phạm Kiều Oanh (NV-OANH) |
| 9 Quyết định | Xong (v2) | C12; tiêu chí hash `45296e79` không đổi; cổng vòng 1 `3c132c2e` còn nguyên | Lê Thanh Tùng (NV-TUNG) |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Dòng "Lỗi ghi oan cho hãng" (`wrongful_carrier_faults`) có trong report, nhưng chỉ đo được khi có nhãn, không dùng được trong production. **Chưa có** tín hiệu không cần nhãn cho "lỗi ghi cho kiện không trễ" và "một hãng nhận dồn lỗi"; nay đã thêm `fault_on_non_late_parcel` và `carrier_faults_max_per_day`. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm: `fault_on_non_late_parcel` ≥ 1 → ĐỎ; `carrier_faults_max_per_day`: 2 → VÀNG, > 2 → ĐỎ (trước đây không đo); `multi_carrier_late_share` > 0,2 → VÀNG. Trần 2 lỗi/hãng/ngày: hành động đổi từ "chuyển người cả ticket" thành "bỏ lệnh ghi lỗi, giữ khoản hoàn". |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Giữ 1 người trực (S6: hàng chờ 0 phút, 0 ca ùn, 2 ca/ngày chuyển người). Thêm: ca "đơn tách kiện không rõ kiện" do NV-HANH duyệt, NV-OANH xác nhận hãng chịu trước khi ghi lỗi tay; NV-OANH là đầu mối nhận khiếu nại của hãng. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Phạm vi giữ "all" (mọi kho đạt, chi phí 659–5.611đ/ticket). Quy trình: đơn tách kiện nhiều hãng mà khách không chỉ rõ kiện → luôn chuyển người, không ghi tự động; lỗi thứ 3+ trong ngày của một hãng → người ghi tay. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | NV-OANH gửi hãng Sông Hồng (và GHSH, DNB) danh sách lỗi ghi oan trong tháng, **huỷ lỗi và đề nghị hoàn thưởng chuyên cần cho tài xế** trong 2 ngày làm việc; báo quy tắc mới (lỗi theo kiện, tối đa 2 lỗi tự động/ngày). NV-HANH báo nhân viên duyệt về loại ca mới "không rõ kiện". |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có lần lộ dữ liệu cá nhân trong thẻ (`pii_leaks = 0` ở cả ba mốc); thông báo gửi hãng đã chỉ còn 4 trường từ cổng vòng 1. Không cần báo. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Lộ ra qua **phản hồi của người** (tin nhắn thoại của trưởng nhóm tài xế qua phòng Đối tác), không qua số máy đo. Bàn chưa có: kênh nhận khiếu nại của hãng / tài xế được ghi lại như một tín hiệu, và metric không cần nhãn cho lỗi hãng (nay đã thêm). |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp **3** lần trong một giờ thì: NV-HANH xem hàng chờ; hàng chờ ≥ 6 ca hoặc chờ lâu nhất ≥ 30 phút → gọi người trực thứ hai (`reviewers_on_shift = 2`, `review_capacity_per_hour = 12`); vẫn có ca chờ > 60 phút trong 2 giờ → NV-TUNG thu hẹp `pilot_scope` (`percent: 50`), ưu tiên loại đơn tách kiện nhiều hãng khỏi phạm vi tự động.
2. Nếu nhà cung cấp LLM lỗi quá **15** phút thì: Cổng 1 đã chuyển người mọi ca `basis ≠ policy` (không fail-open); NV-TUNG thu hẹp `pilot_scope` về 0% tự động trong lúc lỗi (ticket mới làm tay), báo `#logix-refund-pilot-oncall`; khi LLM ổn định 30 phút thì bật lại, kiểm `escalation_rate` trở về ≤ 0,25.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: NV-HANH ghi mã ticket vào kênh; NV-TUNG mở trace trong 1 giờ; nếu quyết định sai → tắt lệnh ghi liên quan theo Runbook 3 và thêm ca vào bộ thử; nếu đúng → bật `operations.decision_note = true` và kiểm mẫu `review_sampling_pct = 10` (điều kiện tin trong `staff_behavior.trust_conditions`) trong một tuần.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `c819e83` (tiêu chí hash `45296e79`, giống v1) |
| Hash chốt cổng vòng 1 | `3c132c2e` (giống v1) |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: R-S6-before-20261119-161405-e2825f · prepared: R-S6-prepared-20261119-161405-e2825f · after: R-S6-after-20261119-161405-e2825f |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không. Report grade `R-S6-grade-20261119-161404-e2825f`: "Không vượt trần kinh doanh / vận hành nào. Mọi ngưỡng đã ký đều đạt." Trên thẻ: hàng chờ 0 phút, 0 ca ùn, chi phí 4.812đ/ticket, ROI 1.08, hoàn sai 0đ, lỗi hãng oan 0, lộ dữ liệu 0. |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Kho **HCM** trên thẻ: chi phí 5.611đ/ticket (cao nhất, vì đơn mơ hồ S6-20, S6-21 chuyển người), pass 1.0. Hãng **GHSH** (base: oan 30, prepared: oan 5), nay 0. Phân khúc `?` của bộ nền 10.359đ/ticket (đơn không tồn tại, luôn chuyển người). Quyết định **không đổi**: HCM vẫn dưới trần 7.000đ và rẻ hơn làm tay. |
| Quyết định (khoanh một) | **Tiếp tục** · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S6-after-20261119-161405-e2825f` (gói S6): cả 5 chỉ số bắt buộc đạt: pass_rate 1.0, pass_k 1.0, hoàn sai 0đ, lỗi hãng oan 0, lộ dữ liệu 0; escalation_rate 0.1667 ≤ 0.25. |
| Bằng chứng 2 | `R-base-after-20261119-161357-e2825f` (bộ nền): 110/110, không regression (`5 regression ✅`); chi phí 4.202đ, ROI 1.38, 0 ca ùn. |
| Bằng chứng 3 | So ba mốc trên thẻ: lỗi hãng oan 40 → 10 → 0; hoàn sai 270.000 → 270.000 → 0đ; ROI 0.74 → 0.14 → 1.08; monitor mới sáng đèn (`fault_on_non_late_parcel` 15 ở base, `carrier_faults_max_per_day` 4 → 2). |
| Khớp dòng nào trong `decision_rule` đã ký? | "Tiếp tục": cả 5 ngưỡng bắt buộc đạt trên bộ nền **VÀ** trên gói sự cố; cost_per_ticket ≤ 7.000đ, ROI ≥ 0.3, không ca nào ùn quá SLA 60 phút; report không còn dòng vượt trần nào. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | (không áp dụng) Pilot ở phạm vi `all`, 1 người trực; riêng nhóm "đơn tách kiện nhiều hãng, khách không chỉ rõ kiện" luôn chuyển NV-HANH (không tự động). |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | (không áp dụng) |
| Nếu Dừng: bài học ghi lại | (không áp dụng) |
| Ngày quyết định lại (trừ khi Dừng) | 2026-11-30 (trước khi REFUND-v4 hiệu lực 01/12/2026); và sau tuần đầu pilot thật. |
| PIC ký | Lê Thanh Tùng (NV-TUNG), PIC trợ lý · đồng ký: vai Sản phẩm và kinh doanh của bàn |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Giữ "Tiếp tục"**. v1 là "Tiếp tục có điều kiện" vì chưa đo gói sự cố; ở mốc prepared, gói S6 **trượt** (hoàn sai 270.000đ, 10 lỗi oan, ROI 0.14), nên nếu dừng ở prepared thì phải đổi sang Cải tiến thêm. Sau khi sửa (after), mọi ngưỡng đã ký đạt trên cả bộ nền và gói sự cố, nên điều kiện của v1 đã được đáp ứng.
- Report tự kiểm tra: mã lần chạy `R-S6-grade-20261119-161404-e2825f` · ô nào còn đỏ (nguyên nhân × tầng): **1 integrity ❌**. Nguyên nhân: môi trường Git trên máy (`core.autocrlf=true`) đổi kiểu xuống dòng của file khoá khi checkout, không phải bàn sửa nội dung; bản trong repo vẫn dùng LF (`git show HEAD:lab10/agent.py` không có CR). Tầng: hạ tầng / môi trường máy. Còn lại: criteria ✅, visible ✅, regression ✅, monitor ✅; hidden "—" (chỉ chạy ở team chấm).
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Đỡ được ghi lỗi cho kiện đầu tiên (lỗi oan 40 → 10, pass 0.33 → 0.67), nhờ dòng HAZOP INCOMPLETE "đơn nhiều kiện" ở Phiếu B mục B4. Bỏ sót: (a) ca nhiều hãng cùng trễ mà không rõ kiện: cổng vẫn đoán "kiện trễ nhất"; (b) trần 2 lỗi/hãng chuyển người sau khi đã hoàn tiền, làm ROI tụt 0.74 → 0.14.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report mốc after ghi **"Được phép cân nhắc 'Tiếp tục'"**; quyết định "Tiếp tục" khớp.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: **Bộ test ẩn** (đơn, khách, cách viết khác) và **đơn tách kiện mà khách ghi sai `parcel_id`**, hoặc hai kiện của **cùng một hãng** cùng trễ. Nếu test ẩn trượt ngưỡng an toàn, v2 phải hạ xuống "Cải tiến thêm" theo đúng `decision_rule`. Gói thẻ chỉ có 12 ticket, nên khoảng tin cậy trên dân số thật còn rộng.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Tracking DB của từng hãng ghi đúng ngày giao và nguyên nhân trễ của từng kiện, và khi khách chỉ rõ mã kiện thì mã đó đúng; cổng của đội tin hoàn toàn hai nguồn này để quyết ai chịu lỗi.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Ngăn được việc hệ thống tự ghi lỗi cho kiện không trễ hoặc tự chọn hãng khi nhiều hãng cùng trễ (cổng tính lại kiện từ tracking và dừng trước lệnh hoàn), nhưng chỉ GIẢM tác hại chung: trần 2 lỗi/hãng/ngày vẫn cho 2 lỗi đầu tự động, và nếu tracking hoặc parcel_id sai thì cổng vẫn ghi sai theo.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Tỉ lệ đơn tách kiện nhiều hãng và số ca "không rõ kiện" chuyển người mỗi ngày (ảnh hưởng hàng chờ và chi phí), số khiếu nại lỗi oan từ hãng mỗi tuần, và độ chính xác của delay_cause trong tracking từng hãng so với đối soát của kế toán.
