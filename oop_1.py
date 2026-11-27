class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calculate_anual_salary(self):
        return  self.salary * 12 

emp = Employee("mohan",50000)

print(emp.name)
print(emp.calculate_anual_salary())