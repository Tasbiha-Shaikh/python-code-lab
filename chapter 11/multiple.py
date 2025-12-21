# base/parent class
class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}") 


class Coder:
    language = "Python"

    def printlanguages(self):
        print(f"Out of all languages, your language is {self.language}")


# inherited class (multiple inheritance)
class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee("Ali", 50000)
b = Programmer("Ahmed", 90000)

b.show()
b.showlanguage()
b.printlanguages()

print(a.company, b.company)
