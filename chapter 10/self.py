class Employee:
    company = "google"

    def getsalary(self):
        print(f"The company is {self.company}")

    @staticmethod
    def greet():
        print("hello user")


harry = Employee()
harry.greet()
harry.getsalary()
