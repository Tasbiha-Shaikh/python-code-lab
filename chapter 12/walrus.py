#using walrus operator :=
if(n := len([1,2,3,4,5]))>3:
    print(f"list is to long ({n} elements,expected <= 3)")


# type definations 

age: int = 25
def greeting(name:str) -> str:
    return f"hello,{name}"

print(greeting("alice"))


def sum(a: int, b: int) -> int:
    return a + b

print(sum(3, 5))
