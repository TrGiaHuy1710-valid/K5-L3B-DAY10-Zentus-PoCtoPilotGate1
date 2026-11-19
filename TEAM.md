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
- 

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

<!-- Long tự viết: việc mình đã làm, con số mình chọn và lý do (bàn phải giải thích được lúc demo). -->
- Ngưỡng trong `config/acceptance_criteria.json`: …
- Con số trong `config/operating_gates.json` (`business`, `operations`, `legal`): …
- Runbook 1–5, giờ cao điểm: …
- Quyết định v1, v2: …
- Dùng AI cho phần nào: …

### Bằng chứng

<!-- Mã commit, mã lần chạy, dòng trong phiếu. -->
- Commit: …
- Phiếu A mục …; Phiếu B mục …; Phiếu C mục …

### Exit ticket

Học được: …

Chưa chắc: …
