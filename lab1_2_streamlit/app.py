import streamlit as st
from PIL import Image
import os

# Trạng thái LED mô phỏng
if "led_on" not in st.session_state:
    st.session_state.led_on = False

# Xử lý sự kiện nút trước khi render
col1, col2 = st.columns(2)
with col1:
    if st.button("BẬT LED"):
        st.session_state.led_on = True
with col2:
    if st.button("TẮT LED"):
        st.session_state.led_on = False

# Sau khi cập nhật trạng thái → render ảnh
st.title("Điều khiển LED mô phỏng bằng Streamlit")

# Đảm bảo rằng thư mục 'images' và các file ảnh tồn tại
led_image = "images/led_on.png" if st.session_state.led_on else "images/led_off.png"

# Kiểm tra sự tồn tại của tệp ảnh
if os.path.exists(led_image):
    image = Image.open(led_image)
    st.image(image, caption="LED is ON" if st.session_state.led_on else "LED is OFF", width=200)
else:
    st.error("Không tìm thấy file ảnh! Vui lòng kiểm tra lại thư mục images.")
