# factorial(n) = n*factorial(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("enter the number:"))
print(f"the factorial of this number is : {factorial(n)}")
    

