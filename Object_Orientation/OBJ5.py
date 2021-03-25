
class Employee:
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}. " \
            f"He took {samrat.no_of_leaves} days leave this month."

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves

    @classmethod
    def from_dash(cls, string):
        #hey = string.split("-")
        #return cls(hey[0], hey[1], hey[2])
        return cls(*string.split("-"))

samrat = Employee("Samrat", 1000000, "CEO")
samrat.change_leaves(36)
nissan = Employee.from_dash("Nissan-50000-Student")

print(samrat.salary)
print(samrat.no_of_leaves)
print(nissan.role)