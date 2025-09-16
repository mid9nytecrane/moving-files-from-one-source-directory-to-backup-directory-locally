import pyotp
import time 

totp = pyotp.TOTP('base32secret3232')
print("Current OTP:", totp.now())

print(f"verify: {totp.verify(totp.now())}")


print('==='*8)

hotp = pyotp.HOTP('base32secret3232')
print(f"hotp.(0): {hotp.at(0)}")
print(f"hotp.at(1): {hotp.at(1)}")
print(f"hotp.at(1402): {hotp.at(1402)}")

print('==='*8)
url_otp = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='alice@google.com', issuer_name='Secure App')
print(url_otp)