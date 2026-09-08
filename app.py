import streamlit as st
from google import genai

# Mã API Key của bạn đã được cấu hình sẵn
API_KEY = "AQ.Ab8RN6IaOft0tzw_2la8R7hz38JmL2hiIadByt672clJhIazrQ"
client = genai.Client(api_key=API_KEY)

# Cấu hình tiêu đề trang web
st.set_page_config(page_title="AI Giải Toán Lớp 1-12", page_icon="🧮")

st.title("🧮 Trợ Lý AI Giải Toán Lớp 1 - 12")
st.write("Nhập đề bài toán vào ô bên dưới, AI sẽ giải chi tiết từng bước cho bạn!")

# Ô nhập đề bài
de_bai = st.text_area("Nhập đề bài toán tại đây:", placeholder="Ví dụ: Tìm x biết 2x + 5 = 15...")

# Nút bấm giải toán
if st.button("Bắt đầu giải toán 🚀", type="primary"):
    if de_bai.strip() == "":
        st.warning("Vui lòng nhập đề bài trước!")
    else:
        with st.spinner("AI đang suy nghĩ và phân tích lời giải..."):
            try:
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=f"Bạn là một giáo viên dạy toán giỏi tại Việt Nam. Hãy giải chi tiết từng bước bài toán sau đây sao cho học sinh từ lớp 1 đến lớp 12 đều có thể dễ dàng hiểu được: {de_bai}",
                )
                st.success("Đã tìm ra lời giải!")
                st.markdown("### 📝 Lời giải chi tiết:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Lỗi kết nối AI: {e}")
