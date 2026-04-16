def add(a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide (a,b):
    return a / b
print("simple calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice = int(input("enter your choice(1-4):"))

num1 = float(input("enter a first number :"))
num2 = float(input("enter a second number :"))
if choice == 1:
    print("result :", add(num1,num2))
elif choice == 2:
    print("result:",subtract (num1,num2))
elif choice == 3:
    print("result:",multiply(num1,num2))
elif choice == 4:
    if num2 !=0:
        print("result:",divide(num1,num2))
    else:
        print("error: division by zero")
else:
    print("invalid choice")
