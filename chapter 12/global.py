# global variable
a = 90
def func():
    global a
    #local variable
    a = 3
    print(a)

func()
print(a)