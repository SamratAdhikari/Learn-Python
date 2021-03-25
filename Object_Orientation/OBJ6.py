
class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}. " \
            f"He took {samrat.no_of_leaves} days leave this month."

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print ("This is good " + string)

samrat = Employee("Samrat", 1000000, "CEO")
samrat.change_leaves(36)
nissan = Employee.from_dash("Nissan-50000-Student")


samrat.printgood("Samrat")