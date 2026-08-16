a=input("Enter Number1: ")
b=input("Enter Number2: ")
try:
    z=a/int(b)
except ZeroDivisionError as e:
    print("exception occured: ",e)
    z=None
except Exception as e:
    print("exception type: ",type(e).__name__)
    z=None
print("division1 is: ",z)