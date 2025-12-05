# n = int(input("enter the number: "))

# i = 1
# total = 0

# while i <= n:
#     total += i
#     i += 1

# print( total)


#factorial
#5! = 1*2*3*4*5

n = int(input("enter a number : "))
product = 1

for i in range(1 , n+1):
    product = product * i

    print(f"the factorial of  {n} is {product}")


