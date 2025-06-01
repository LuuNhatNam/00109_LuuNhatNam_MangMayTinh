import hashlib
import pyotp
import time


# Mật khẩu lưu trữ dưới dạng mã băm SHA-256
stored_password = hashlib.sha256(b"123456nam").hexdigest()
# Yêu cầu người dùng nhập mật khẩu
password = input("Nhập mật khẩu: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()
if hashed_password == stored_password:
    print("Xác thực thành công!")
else:
    print("Xác thực thất bại!")