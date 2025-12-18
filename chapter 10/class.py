class Employee:
    name = "harry" # this is class attribute
    language = "python" 
    salary = 1200000

harry = Employee()
harry.name = "rohan" # this is instance attribute
print(harry.name,harry.salary)



#name is object/instance attribute and salary and language are class attribute as they directly belong to the class


class Employee:
    company = "google"

harry = Employee()
Employee.company = "youtube"
print(harry.company)
print(Employee.company)