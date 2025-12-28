class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContext():
    print("Inside the context")


#exc_type = type of exception
#exc_value = exception value
#tracebook = tracebook details
