
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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    def __init__(self, name, salary, role, language):
        #super().__init__(name, salary, role)
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language

    def print_prog(self):
        print (f"Name of Programmer is {self.name}. Salary is {self.salary} and role is {self.role}. "
               f"He took {samrat.no_of_leaves} days leave this month. The languages are {self.language}")




samrat = Employee("Samrat", 1000000, "CEO")
samrat.change_leaves(36)
nissan = Employee.from_dash("Nissan-50000-Student")
dipu = Programmer("Dipesh", 546464, "Programmer", ["Python", "Java"])
bidhan = Programmer("Bidhan", 564651, "Programmer", ["Python"])
dipu.print_prog()
print(bidhan.printdetails())

samrat.printgood("Samrat")