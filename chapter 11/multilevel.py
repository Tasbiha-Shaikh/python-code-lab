# Base / Parent class
class Employee:
    company = "ITC"
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"Employee name: {self.name}")


# Derived class (Child of Employee)
class Coder(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def show_language(self):
        print(f"Language: {self.language}")


# Derived class (Child of Coder)
class Programmer(Coder):
    def __init__(self, name, language, salary):
        super().__init__(name, language)
        self.salary = salary

    def show_salary(self):
        print(f"Salary: {self.salary}")


# Object of most derived class
p = Programmer("Ahmed", "Python", 80000)

p.show()
p.show_language()
p.show_salary()
