import pyotp
import time
# Tạo khóa bí mật và mã OTP
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)
print("Mã OTP của bạn là:", totp.now())
# Yêu cầu nhập mã OTP
otp_input = input("Nhập mã OTP: ")
if totp.verify(otp_input):
    print("Xác thực thành công!")
else:
    print("Xác thực thất bại!")