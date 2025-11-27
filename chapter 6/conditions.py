a = int(input("enter your age:"))

if(a>18):
    print("you are above the age of concent")

else:
    print("you are below the age of concent")


# if else elif ladder
a = int(input("enter your age:"))

if(a>=18):
    print("you are above the age of concent")

elif(a<0):
    print("you are entering invalid age")

elif(a==0):
    print("you are entering 0 is not a valid age")

else:
    print("you are below the age of concent")