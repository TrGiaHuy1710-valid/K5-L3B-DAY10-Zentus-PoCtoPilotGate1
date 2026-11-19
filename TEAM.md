# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Zentus
- Lớp: `L3B`
- Repo của bàn: https://github.com/TrGiaHuy1710-valid/K5-L3B-DAY10-Zentus-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trịnh Gia Huy | 2A202603924 | Kỹ sư cổng | X |
|   2 | Trần Bảo Long | 2A202604012 | Sản phẩm và kinh doanh · Vận hành và pháp lý | |
|   3 | | | | |
|   4 | | | | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

Bàn 2 người (README quy định 3–4): Long giữ hai vai không phải code.

## Báo cáo của bàn

### Kết quả

| Mốc | Bộ | pass_rate | Hoàn sai | Lỗi hãng oan | Lộ dữ liệu | ROI | Mã lần chạy |
|---|---|---|---|---|---|---|---|
| base | bộ nền | 0.9909 | 20.000đ | 1 | 0 | 1.34 | `R-base-before-20261119-152308-bde05c` |
| prepared | bộ nền | 1.0 | 0 | 0 | 0 | 1.38 | `R-base-prepared-20261119-152542-2b41c3` |
| base | S6 | 0.3333 | 270.000đ | 40 | 0 | 0.74 | `R-S6-before-20261119-161405-e2825f` |
| prepared | S6 | 0.6667 | 270.000đ | 10 | 0 | 0.14 | `R-S6-prepared-20261119-161405-e2825f` |
| after | S6 | 1.0 | 0 | 0 | 0 | 1.08 | `R-S6-after-20261119-161405-e2825f` |

Tự kiểm tra: `PASS-VISIBLE`. Quyết định v1: Tiếp tục (có điều kiện chờ gói sự cố). Quyết định v2: Tiếp tục.

### Phần đã làm

**Kỹ sư cổng · Trịnh Gia Huy**
- Chạy mốc base, đọc report và `lab10.gate`, trace `T-002@55` (Phiếu B mục B0–B2).
- HAZOP vòng 1 trên `file_carrier_fault` (B4), pre-mortem (B6), cổng vòng 1 và behavioral test (B7.1–B7.3).
- `lab10/guards.py` vòng 1: Cổng 0 (ghim chính sách theo ngày hiệu lực), Cổng 1 (`issue_refund` theo quyền lợi tính từ tracking, phê duyệt hợp lệ, không hoàn lặp, trần ngày), Cổng 2 (`file_carrier_fault` theo kiện trễ và nguyên nhân ghi nhận, trần 2 lỗi/hãng/ngày), Cổng 3 (`notify_carrier` chỉ gửi 4 trường cho phép).
- Chốt vòng 1 (`3c132c2e`), đo mốc prepared.
- Nhận thẻ S6, trace S6-01, S6-04, S6-20, S6-21, S6-42; sửa cổng vòng 2 (đơn tách kiện nhiều hãng cùng trễ → chuyển người trước khi hoàn; trần lỗi/hãng → bỏ lệnh ghi lỗi thay vì escalate; ghi lỗi theo kiện khách chỉ rõ).
- `lab10/monitors.py`: `fault_on_non_late_parcel`, `multi_carrier_late_share`, `carrier_faults_max_per_day`.
- Phiếu C mục C0–C2, C4, C6–C9; chạy `lab10.grade`, `check_submission --collect`.
- Sửa lỗi kiểu xuống dòng CRLF làm hỏng kiểm tra integrity trên máy Windows.

**Sản phẩm và kinh doanh · Vận hành và pháp lý · Trần Bảo Long**
- Xác định mục tiêu cấp hệ thống, thước đo telemetry production, tiêu chí chấp nhận và ký `config/acceptance_criteria.json` trước khi chạy đánh giá (Phiếu A mục A1–A5).
- Lập bản đồ dữ liệu, ví dụ drift, HAZOP phần ngoài kỹ thuật và checklist 9 nhóm có PIC (Phiếu B mục B3–B5).
- Đặt con số cổng kinh doanh, vận hành, pháp lý trong `config/operating_gates.json` và viết Runbook phần 1–3, mục Giờ cao điểm (B7.4–B7.6).
- Tham gia quyết định v1 (B8), cập nhật giả định môi trường, risk register, checklist và Runbook 4–5 sau thẻ S6, rồi chốt quyết định v2, ba dòng bắt buộc và `submission/submission.json` (Phiếu C mục C5, C10–C12).

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TrinhGiaHuy-2A202603924

### Phần việc phụ trách

Kỹ sư cổng. Câu 2.1, 2.2, 2.6–2.8 (Phiếu B mục B0–B2, B4, B6, B7.1–B7.3, B8); câu 3.0, 3.1, 3.4–3.7 (Phiếu C mục C0–C2, C4, C6–C9). File: `lab10/guards.py`, `lab10/monitors.py`. Trưởng nhóm: tạo repo, ký và đẩy tiêu chí, chốt vòng 1, nhận thẻ, gom bài nộp.

### Đóng góp cụ thể

- Cổng vòng 1 đưa bộ nền từ 2 ngưỡng an toàn trượt (hoàn sai 20.000đ, 1 lỗi oan cho VNX ở `T-002@55`) về 9/9 ngưỡng đạt, không làm hỏng ca nào đang đúng.
- Một lần thử cổng làm hỏng 60 ca đúng (pass_rate 0.45) vì so `customer_id` trong `action` mà tool không truyền; tìm ra qua trace `T-001@11`, sửa sang `ctx.ticket`.
- Cổng vòng 1 đỡ trước 30/40 lỗi oan của thẻ S6 (ghi lỗi theo kiện trễ thay vì kiện đầu tiên).
- Vòng 2 xử lý hai nhánh còn lại: đơn có ≥ 2 hãng cùng trễ mà khách không chỉ rõ kiện, và trần lỗi escalate sau khi tiền đã ghi. Gói S6 về 0 hoàn sai, 0 lỗi oan, ROI 0.14 → 1.08.
- 3 monitor không cần nhãn, sáng đèn trên S6 (`fault_on_non_late_parcel` 0 → 15 ở base, `carrier_faults_max_per_day` 4 → 2).
- Dùng AI (Claude Code) để đọc code agent, gợi ý cách viết cổng và monitor, soạn nháp các mục phiếu B, C. Ngưỡng, quyết định và cổng đã được kiểm lại bằng lần chạy và trace trước khi giữ.

### Bằng chứng

| Commit | Thời gian | Nội dung |
|---|---|---|
| `c819e83` | 15:11 19/11 | Sign acceptance criteria |
| `4e7b70b` | 15:22 19/11 | criteria report |
| `c8df97a` | 15:53 19/11 | Chốt cổng vòng 1, quyết định v1 |
| `78f99d3` | 16:12 19/11 | Nhận thẻ S6 |
| `ba88ae6` | 16:38 19/11 | Bài nộp |

- Tiêu chí hash `45296e79`; chốt vòng 1 `3c132c2e`.
- Lần chạy: `R-base-before-20261119-152308-bde05c`, `R-base-after-20261119-152525-2b41c3`, `R-base-prepared-20261119-152542-2b41c3`, `R-S6-after-20261119-161356-e2825f`, `R-base-after-20261119-161357-e2825f`, grade `R-S6-grade-20261119-161404-e2825f`.
- Phiếu B mục B0 (dòng 1–6), B7.1; Phiếu C mục C0, C7, C8.

### Exit ticket

Học được: cổng phải dựa trên nguồn sự thật và đặt trước lệnh ghi đầu tiên; cổng đặt sau lệnh ghi tiền (trần lỗi/hãng ở vòng 1) vẫn gây trạng thái lệch dù chặn đúng.

Chưa chắc: cổng S6 tin hoàn toàn tracking và `parcel_id` khách khai; chưa biết bộ test ẩn có ca tracking sai hoặc hai kiện cùng một hãng trễ hay không.

## TranBaoLong-2A202604012

### Phần việc phụ trách

<!-- Long hoàn thiện. Gợi ý theo phân công: -->
Sản phẩm và kinh doanh · Vận hành và pháp lý. Câu 1.1–1.6 (Phiếu A), 2.3, 2.4, 2.9, 2.10 (Phiếu B mục B3, B4 phần ngoài kỹ thuật, B5, B7.4–B7.6), quyết định v1 (B8); câu 3.1 phần riêng (Phiếu C mục C3.2), C5, C10–C12. File: `config/acceptance_criteria.json`, `config/operating_gates.json`, `submission/submission.json`.

### Đóng góp cụ thể

- Ngưỡng trong `config/acceptance_criteria.json`: đặt ba ngưỡng an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) bằng `0` vì mỗi lỗi sai đều gây thiệt hại trực tiếp cho LogiX, hãng vận chuyển hoặc vi phạm pháp lý; `pass_rate_min = 0.9` và `pass_k_min = 0.85` (110 lần chạy có khoảng tin cậy ±5% nên không siết quá chặt); `escalation_rate_max = 0.25`, `cost_per_ticket_vnd_max = 7000` (thấp hơn làm tay 10.000đ), `roi_min = 0.3`, `queue_stuck_max = 0`, kèm 4 quy tắc `decision_rule` rõ ràng.
- Con số trong `config/operating_gates.json` (`business`, `operations`, `legal`): `daily_refund_cap_vnd = 1500000` (75% ngân sách Finance 2.000.000đ/ngày, chừa 500.000đ cho ca duyệt tay), `cost_budget_per_ticket_vnd = 1500`, `pilot_scope = all (100%)`, `roi_min = 0.3`; `reviewers_on_shift = 1` (NV-HANH, công suất 6 ca/giờ, `max_queue_wait_minutes = 60`), PIC `NV-TUNG`, 4 `stop_conditions` (tắt trong 15 phút), kênh `#logix-refund-pilot-oncall`; chặn 6 trường PII gửi bên thứ ba và bật `carrier_fault_requires_recorded_cause = true`.
- Runbook 1–5, giờ cao điểm: phân rõ 4 vai (NV-TUNG giữ công tắc/PIC, NV-HANH duyệt vượt hạn mức, NV-OANH nhận khiếu nại hãng/shop), bảng tín hiệu VÀNG/ĐỎ khớp report và 3 monitor mới; giờ cao điểm (ngày sale, sau bão) nâng lên 2 người trực khi hàng chờ ≥ 6 ca hoặc chờ ≥ 30 phút (phí giữ chỗ 30.000đ/ca); Runbook 4–5 bổ sung quy trình NV-OANH huỷ lỗi oan với hãng Sông Hồng trong 2 ngày làm việc và 3 kịch bản ứng phó tuần đầu pilot.
- Quyết định v1, v2: v1 chọn **Tiếp tục** (có điều kiện chờ thẻ sự cố) dựa trên `R-base-prepared-20261119-152542-2b41c3` đạt 9/9 ngưỡng; v2 giữ **Tiếp tục** vì sau sửa vòng 2, thẻ S6 (`R-S6-after-20261119-161405-e2825f`) và bộ nền (`R-base-after-20261119-161357-e2825f`) đều đạt mọi ngưỡng, hoàn sai = 0, lỗi oan = 0, ROI = 1.08.
- Dùng AI cho phần nào: dùng trợ lý AI để rà soát sự nhất quán giữa các con số trong `config/`, runbook và các mục Phiếu A, B, C, cũng như hỗ trợ tổng hợp nháp mục cá nhân từ kết quả repo; toàn bộ ngưỡng, lý do kinh doanh/vận hành và quyết định Gate 1 đã được kiểm tra đối chiếu lại với `data/world.json` và report trước khi giữ.

### Bằng chứng

- Commit cá nhân: `05d1b1e` (`TEAM.md`).
- Tiêu chí hash `45296e79` (ký trước khi đo `base`); chốt vòng 1 `3c132c2e`.
- Mã lần chạy đối chiếu cho quyết định v1, v2: `R-base-prepared-20261119-152542-2b41c3`, `R-S6-after-20261119-161405-e2825f`, `R-base-after-20261119-161357-e2825f`.
- Phiếu A mục A1–A5; Phiếu B mục B3–B5, B7.4–B7.6 (có tên người viết ở B7.5), B8; Phiếu C mục C5, C10–C12; `config/acceptance_criteria.json`, `config/operating_gates.json`, `submission/submission.json`.

### Exit ticket

Học được: tiêu chí chấp nhận phải được chốt và ký trước khi xem kết quả đo để tránh chỉnh ngưỡng theo số; một Gate 1 đạt chuẩn không chỉ nằm ở code chặn lỗi mà còn ở trần tiền, công suất người trực, quy trình xử lý sự cố với bên thứ ba và điều kiện dừng rõ ràng.

Chưa chắc: khi chạy pilot thật với lượng ticket biến động mạnh (ngày sale hoặc sau bão), tỉ lệ ca chuyển người từ đơn tách kiện nhiều hãng có làm quá tải 1 người trực (6 ca/giờ) và kéo ROI xuống dưới 0.3 hay không, cần theo dõi sát qua tuần đầu.
