from functools import reduce

l = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, l))

print(squares)

#filter example
def even(n):
    if(n%2 == 0):
        return True
    return False

Even  = filter(even,l)
print(list(Even))


#reduce function
def sum(a,b):
    return a+b

print(reduce(sum,l))



from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# square all numbers
squares = list(map(lambda x: x*x, numbers))

# filter even squares
even_squares = list(filter(lambda x: x % 2 == 0, squares))

# sum of even squares
result = reduce(lambda x, y: x + y, even_squares)

print(result)
