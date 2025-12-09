# # def greet(name):
# #     print("hello"+name)

# # greet("harry")


# def greet(name):
#     gr = "hello" + name
#     return gr

# a = greet("harry")
# print(a)



# default parameter value 

def greet(name , ending = "thank you"):
    print(f"good day, {name}")
    print(ending)

greet("harry")