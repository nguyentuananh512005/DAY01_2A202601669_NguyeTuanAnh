# K3 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 9h00–13h00
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng placeholder bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> **Kết quả thực tế (model: gemini-2.5-flash):**
> - **temperature = 0.0 (6.33s):** "Việt Nam là nơi có **hang động lớn nhất thế giới – Hang Sơn Đoòng**. Nằm..."
> - **temperature = 0.5:** (bị rate limit do free tier giới hạn 5 request/phút)
> - **temperature = 1.0 (5.76s):** "Việt Nam là nơi có hang động lớn nhất thế giới – Hang Sơn Đoòng. Nằm trong V..."
> - **temperature = 1.5 (6.50s):** "Việt Nam có **Hang Sơn Đoòng**, nằm trong Vườn Quốc gia Phong Nha-Kẻ Bàng. Đây..."
>
> **Nhận xét:** Với gemini-2.5-flash (thinking model), cả 3 mức temperature đều cho cùng chủ đề Hang Sơn Đoòng — khác với model non-thinking ở chỗ quá trình "suy nghĩ" bên trong giúp ổn định output, khiến temperature ít ảnh hưởng hơn. Tuy nhiên, cách diễn đạt vẫn thay đổi nhẹ: temperature 0.0 dùng dấu ** in đậm và cấu trúc chuẩn, còn temperature 1.5 thì dùng cách mở đầu khác và linh hoạt hơn trong cách trình bày. Với model non-thinking thông thường, sự khác biệt sẽ rõ hơn nhiều — temperature cao sẽ cho ra chủ đề khác nhau và đôi khi thiếu mạch lạc.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ luôn đặt **temperature = 0** cho chatbot chăm sóc khách hàng. Lý do quan trọng nhất: khi temperature > 0, AI có xu hướng "sáng tạo" và có thể bịa ra những quyền lợi, tác dụng hoặc chính sách của sản phẩm mà công ty thực tế không có (hallucination). Điều này cực kỳ nguy hiểm trong môi trường kinh doanh — nếu chatbot hứa hẹn sai về sản phẩm, công ty phải chịu trách nhiệm pháp lý và mất uy tín với khách hàng. Temperature = 0 đảm bảo câu trả lời luôn ổn định, nhất quán và bám sát dữ kiện được cung cấp, giảm thiểu tối đa rủi ro sai lệch thông tin.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> **Tính toán lý thuyết (GPT-4o vs GPT-4o-mini):**
> - Tổng output/ngày: 10,000 × 3 × 350 = 10,500,000 token
> - GPT-4o: $0.010/1K → $105/ngày
> - GPT-4o-mini: $0.0006/1K → $6.3/ngày
> - **GPT-4o đắt hơn khoảng 16.7 lần**
>
> **Kết quả thực tế so sánh 2 model Gemini (thay thế GPT):**
> Prompt: "Giải thích sự khác biệt giữa temperature và top_p trong một câu."
> - **gemini-2.5-flash (5.75s):** "Temperature kiểm soát độ ngẫu nhiên bằng cách làm thay đổi phân phối xác suất tổng thể của tất cả các từ, trong khi top_p chọn ra một tập hợp các từ có xác suất tích lũy cao nhất để lấy mẫu, giới hạn phạm vi lựa chọn."
> - **gemini-3.5-flash-lite (1.18s):** "Temperature kiểm soát mức độ sáng tạo và ngẫu nhiên của câu trả lời (giá trị càng cao, câu trả lời càng lạ và đa dạng), trong khi top_p kiểm soát độ tập trung của từ vựng bằng cách giới hạn lựa chọn trong một nhóm các từ có xác suất xuất hiện cao nhất (giá trị càng cao, từ vựng càng phong phú)."
>
> **Nhận xét:** gemini-2.5-flash cho câu trả lời ngắn gọn, kỹ thuật hơn nhưng chậm gấp ~5 lần (5.75s vs 1.18s). gemini-3.5-flash-lite trả lời nhanh hơn, dễ hiểu hơn và đầy đủ hơn — cho thấy model lớn không phải lúc nào cũng tốt hơn, đặc biệt khi câu hỏi đơn giản. Trường hợp xứng đáng dùng model lớn: phân tích hợp đồng pháp lý, suy luận phức tạp. Nên dùng model nhỏ: FAQ, tóm tắt, phân loại nội dung.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> **Kết quả thực tế (model: gemini-2.5-flash):**
> - **Giáo viên tiểu học (6.40s):** "Chào các con! Hôm nay cô sẽ kể cho các con nghe về một thứ rất hay ho mà người lớn hay dùng, gọi là 'Blockchain' nhé! Nghe thì khó, nhưng thật..."
> - **Chuyên gia tài chính (5.67s):** "Kính gửi quý vị, Với vai trò là một chuyên gia tài chính, tôi xin trình bày một phân tích chuyên sâu về công nghệ Blockchain, sử dụng các thuật ngữ kỹ thuật..."
>
> **Nhận xét:** Sự khác biệt rất rõ ràng ngay từ cách mở đầu: persona giáo viên dùng "Chào các con!" với giọng thân thiện, gần gũi trẻ em; persona chuyên gia dùng "Kính gửi quý vị" với văn phong trang trọng, chuyên nghiệp. Từ vựng cũng hoàn toàn khác: giáo viên dùng "thứ rất hay ho", "người lớn hay dùng"; chuyên gia dùng "phân tích chuyên sâu", "thuật ngữ kỹ thuật". Điều này chứng minh system prompt hoạt động như "đạo diễn" — cùng một câu hỏi, model tự điều chỉnh toàn bộ phong cách, cấu trúc và độ sâu nội dung dựa trên persona được gán. Đây là công cụ cực kỳ mạnh khi xây dựng sản phẩm — chỉ cần thay system prompt là phục vụ được nhiều đối tượng khác nhau mà không cần fine-tune model.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Với một đoạn văn tiếng Việt ~100 từ, tiktoken đếm được khoảng 180–220 token, trong khi ước lượng bằng số từ/0.75 chỉ cho ra khoảng 133 token — chênh lệch khoảng 35–65%. Tiếng Việt tốn nhiều token hơn tiếng Anh vì tokenizer của OpenAI (BPE) được huấn luyện chủ yếu trên corpus tiếng Anh, nên các từ tiếng Anh phổ biến thường được mã hóa thành 1 token, trong khi tiếng Việt có dấu thanh (ă, ơ, ê, ử, ễ...) và nhiều ký tự đặc biệt khiến mỗi từ bị tách thành 2–4 token. Đây là lý do quan trọng cần dùng tiktoken thay vì ước lượng thô khi tính chi phí cho ứng dụng tiếng Việt.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất khi phản hồi dài và người dùng đang chờ theo thời gian thực — ví dụ chatbot trò chuyện, trợ lý viết văn bản, hoặc giải thích code dài. Khi stream, token đầu tiên xuất hiện ngay (Time To First Token thấp), người dùng thấy kết quả "chạy" liên tục nên cảm giác nhanh hơn nhiều dù tổng thời gian xử lý giống nhau — đây là yếu tố UX rất quan trọng. Ngược lại, non-streaming phù hợp hơn khi cần xử lý hậu kỳ toàn bộ output trước khi hiển thị (ví dụ: trích xuất JSON, phân loại nội dung, kiểm duyệt), hoặc trong pipeline tự động (batch processing) nơi không có người dùng trực tiếp chờ đợi — lúc đó code đơn giản hơn và dễ xử lý lỗi hơn.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff tăng thời gian chờ gấp đôi sau mỗi lần thất bại (0.1s → 0.2s → 0.4s → 0.8s...), giúp giảm tải cho server theo thời gian — càng lỗi lâu càng chờ lâu, cho server cơ hội hồi phục. Nếu hàng nghìn client cùng retry với delay cố định 1 giây, tất cả sẽ đồng loạt gửi lại request đúng sau 1 giây, tạo ra hiện tượng "thundering herd" — đợt sóng request đồng bộ lặp đi lặp lại mỗi giây, khiến server vừa hồi phục lại bị quá tải ngay, có thể gây sập hoàn toàn. Exponential backoff phân tán các retry theo thời gian (mỗi client chờ khác nhau tùy số lần đã thử), giúp server phục hồi dần dần.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Persona: "Bạn là trợ giảng thân thiện của khóa AI, trả lời ngắn gọn bằng tiếng Việt." Tôi chọn "trả lời ngắn gọn" vì trong chatbot CLI, câu trả lời quá dài sẽ tràn terminal và khó đọc, đồng thời giảm chi phí token output — đây là sự cân bằng giữa chất lượng và hiệu quả. Chỉ định "bằng tiếng Việt" là quan trọng vì model mặc định có xu hướng trả lời bằng tiếng Anh; nếu không yêu cầu rõ ràng, model sẽ trộn lẫn ngôn ngữ hoặc chuyển sang tiếng Anh khi gặp thuật ngữ kỹ thuật, gây trải nghiệm không nhất quán cho người dùng Việt Nam.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế lớn nhất là history chỉ giữ 3 lượt cuối (6 message), nên trợ lý "quên" toàn bộ ngữ cảnh trước đó — trong cuộc trò chuyện dài, nó không nhớ người dùng đã hỏi gì ở đầu buổi. Cải thiện đề xuất: thêm cơ chế "tóm tắt lịch sử" (summarization) — thay vì xóa hẳn history cũ, dùng một lời gọi API phụ để tóm tắt các lượt hội thoại bị cắt thành 1 message ngắn, rồi chèn vào đầu history dưới dạng `{"role": "system", "content": "Tóm tắt cuộc trò chuyện trước: ..."}`. Cách này giữ được ngữ cảnh dài hạn mà không tốn quá nhiều token input.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/` và zip theo hướng dẫn README
