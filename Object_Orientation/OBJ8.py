# Public, Private and Protected Access Specifiers
""""
Public - Information that can be accessed only by everyone
Protected - Information that can be accessed only by the family members
Private - Information that can be accessed only by the user(single user)
"""

class Employee:
    no_of_leaves = 10
    _protec = 9
    __private = 98
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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
sam = Employee("Samrat", 1000, "Programmer")
print(sam._protec)
print(sam._Employee__private)