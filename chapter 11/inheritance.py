
#this is base/parent calss
class employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}") 


# class programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

#         def showlanguage(self):
#             print(f"the name is {self.name} and he is good with{self.language} language")

#ths is inheritance class
class programmer(employee):
     company = "ITC infotech"
     def showlanguage(self):
        print(f"the name is {self.name} and he is good with{self.language} language")

a = employee()
b = programmer()

print(a.company,b.company)