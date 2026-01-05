from functools import reduce
a = [111,555,666,435]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,a))