try:
    a = float(input("enter first number:"))
    b = float(input("enter second number:"))
    print("result:",a/b)
except zerodivisionerror:
    print("cannot divisible by zero !")
except ValueError:
    print("please enter numbers only !")
    
