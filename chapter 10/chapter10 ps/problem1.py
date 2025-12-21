class Programmer:
    company = "microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("rohan", 1200000, 234501)
print(p.name, p.salary, p.pin, p.company)
