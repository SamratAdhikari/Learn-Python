
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

samrat = Employee("Samrat", 1000000, "CEO")
samrat.change_leaves(36)


#Employee.no_of_leaves = 69
#print(Employee.no_of_leaves)

print(samrat.printdetails())

print(samrat.salary)
print(samrat.no_of_leaves)