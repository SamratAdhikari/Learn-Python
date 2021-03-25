# Operator Overloading

class Employee:
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}. " \
               f"He took {self.no_of_leaves} days leave this month."

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', '{self.salary}', '{self.role}')"

    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}. " \
               f"He took {self.no_of_leaves} days leave this month."

e1 = Employee("Samrat", 100000, "Programmer")
#e2 = Employee("Cruz", 50000, "Player")
#print(e1 + e2)
#print(e1 / e2)

print(repr(e1))
print(e1)
