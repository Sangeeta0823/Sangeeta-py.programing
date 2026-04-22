import re
phone = input("enter phone number:")
email = input("enter email ID :")

phone_pattern = "^[6-9]\d[9]$"
email_pattern = r"^\w+@\w+\.\w{2,}$"

if re.match(phone_pattern,phone):
    print("valid phone number")
else:
    print("invalid phone number")

if re.match(email_pattern,email):
    print("valid email ID")
else:
    print("invalid email id")
