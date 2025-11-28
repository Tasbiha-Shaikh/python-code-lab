# a = int(input("enter the age :"))

# if(a>=18):
#     print("yes")
# else:
#     print("no")


# multile if statements

a = int(input("enter your age:"))

# if statement no 1
if(a%2==0):
    print("a is even")

# if statement no 2
if(a>=18):
    print("you are above the age of concent")

elif(a<0):
    print("you are entering invalid age")

elif(a==0):
    print("you are entering 0 is not a valid age")

else:
    print("you are below the age of concent")

print("end of program")
