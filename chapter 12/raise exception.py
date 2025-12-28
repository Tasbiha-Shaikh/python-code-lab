a = int(input("enter a number:"))
b = int(input("enter a number:"))
if(b==0):
    raise ZeroDivisionError("heyy")
else:
    print(f"the division of {a/b} is")

#try  with else

try:
    x = int(input("hey enter the number:"))
    print(x)
except Exception as e:
    print(e)

else:
    print("heyy")
