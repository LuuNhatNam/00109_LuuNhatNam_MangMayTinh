import hashlib
import pyotp
import time

# Bước 1: Xác thực bằng mật khẩu
stored_password = hashlib.sha256(b"123456nam").hexdigest()  # Mật khẩu lưu trữ dưới dạng mã băm SHA-256

password = input("Nhập mật khẩu: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()

if hashed_password == stored_password:
    print("Xác thực mật khẩu thành công! Chuyển sang bước xác thực bằng mã OTP.")
else:
    print("Xác thực mật khẩu thất bại!")
    exit()  # Thoát chương trình nếu sai mật khẩu

# Bước 2: Xác thực bằng mã OTP nếu mật khẩu đúng
# Tạo khóa bí mật và mã OTP
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)

# In mã OTP (thực tế sẽ được gửi qua SMS hoặc Email)
print("Mã OTP của bạn là:", totp.now())

# Yêu cầu người dùng nhập mã OTP
otp_input = input("Nhập mã OTP: ")

if totp.verify(otp_input):
    print("Xác thực hai yếu tố thành công!")
else:
    print("Xác thực bước 2, mã OTP thất bại!")
