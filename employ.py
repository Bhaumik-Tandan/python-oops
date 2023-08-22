"""
Question 8: Class Attributes and Methods
Create a class Employee with a class attribute raise_amount and a method apply_raise(). 
Implement a subclass Manager that inherits from Employee. 
Override the apply_raise() method for managers to give them an additional raise.
"""

class Employee:
    raise_amount = 1.04

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def apply_raise(self):
        self.salary = self.salary * self.raise_amount

class Manager(Employee):
    raise_amount = 1.10

    def __init__(self, name, salary, employees=None):
        super().__init__(name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    
    def print_employees(self):
        for employee in self.employees:
            print("-->", employee.name)

emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)

mgr1 = Manager("Sue", 90000, [emp1])
mgr1.add_employee(emp2)
mgr1.print_employees()



    