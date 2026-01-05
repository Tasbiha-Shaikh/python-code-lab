def divisible5(n):
    if(n%5 == 0):
        return True
    return False

n = [1,2,5,10,25]
f = list(filter(divisible5,n))
print(f)