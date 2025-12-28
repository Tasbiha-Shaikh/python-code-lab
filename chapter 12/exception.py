try:
    x = int(input("hey enter the number:"))
    print(x)
except Exception as e:
    print(e)


try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Number cannot be zero")






