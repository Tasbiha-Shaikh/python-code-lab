class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


emp1 = Employee("Harry", 50000)
emp1.get_details()
