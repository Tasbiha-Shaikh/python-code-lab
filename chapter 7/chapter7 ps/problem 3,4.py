# n = int(input("enter a number:"))

# i = 1
# while(i<11):
#     print(f"{n} * {i} = {n * i}")
#     i = i+1


n = int(input("enter a number:"))

for i in range(2,n):
    if(n%i) == 0:
        print("number is not prime")
        break
    else:
        print("number is prime")
