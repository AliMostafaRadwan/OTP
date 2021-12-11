import os
import math
import random
import smtplib

digits="0123456789"
OTP = "".join(digits[math.floor(random.random()*10)] for _ in range(6))
otp = OTP + " <<<<<<<"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your email","your password")
emailid = input("Enter your email: ") # the email to send to
s.sendmail('Your email',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
