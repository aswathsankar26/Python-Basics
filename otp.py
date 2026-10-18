import random

Num1 = int (input("Enter Your Mobile Number : "))

print ("Can I Generate OTP ? (Yes or No) ")

num2  = input()

if num2.strip().lower() == "yes":
    print("wait")
    otp = random.randint(100000 , 999999)
    print ("The OTP is : " , otp)

else:
    print("Session Failed")

