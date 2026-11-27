class Employee:
    company = "ABC Technologies"

    def __init__(self,name):
        self.name = name


emp1 = Employee('mohan')
emp2 = Employee("Akash")

print(emp1.company)
print(emp2.company)