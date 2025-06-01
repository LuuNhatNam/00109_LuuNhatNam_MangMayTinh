import hashlib
import pyotp
import time
import qrcode

# === BƯỚC 1: XÁC THỰC MẬT KHẨU ===

# Giả sử đây là mật khẩu đúng đã lưu (bạn đặt sẵn)
stored_password = hashlib.sha256(b"mypassword").hexdigest()

# Nhập mật khẩu
password = input("Nhập mật khẩu: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()

if hashed_password != stored_password:
    print("Sai mật khẩu! Thoát chương trình.")
    exit()
else:
    print("Mật khẩu đúng! Tiếp tục sang bước xác thực OTP.")

# === BƯỚC 2: XÁC THỰC OTP ===

# Giả sử người dùng đã đăng ký tài khoản => ta sinh secret lưu lại
# Trong thực tế, secret này chỉ sinh một lần và lưu vào DB
secret = pyotp.random_base32()

# Tạo đối tượng OTP
totp = pyotp.TOTP(secret)

# Sinh mã URI tương thích Google Authenticator
otp_uri = totp.provisioning_uri(name="username@example.com", issuer_name="DemoMFA App")

# Sinh QR code từ URI (dùng app Google Authenticator để quét)
img = qrcode.make(otp_uri)
img.save("otp_qr.png")
print("Đã tạo QR code. Hãy quét ảnh 'otp_qr.png' bằng Google Authenticator.")

# Đợi 20 giây để người dùng quét QR
print("Đang chờ bạn quét mã QR bằng ứng dụng OTP...")
time.sleep(20)

# Nhập mã OTP từ người dùng
otp_input = input("Nhập mã OTP hiển thị trên ứng dụng: ")

# Xác thực mã
if totp.verify(otp_input):
    print("Xác thực đa yếu tố (MFA) thành công!")
else:
    print("Mã OTP không hợp lệ! Thoát.")
