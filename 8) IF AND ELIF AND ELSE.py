num=input("enter a number: ")
num=int(num)
if num%2==0:
    print("number is even")
else:
    print("number is odd")


#second program
indian=["samosa","daal","naan"]
chinese=["egg role","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("enter a dish name: ")

if dish in indian:
    print("indian dish")
elif dish in chinese:
    print("chinese dish")
elif dish in italian:
    print("italian dish")
else:
    print("based on little knowledge i have i dont know which cuisine is",dish)
