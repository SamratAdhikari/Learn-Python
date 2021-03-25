
class Employee:
    no_of_leaves = 10
    #def __init__(self, name, salary, role):
        #self.name = name
        #self.salary = salary
        #self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}. " \
            f"He took {samrat.no_of_leaves} days leave this month."

#samrat = Employee("Samrat", 1000000, "CEO" )
samrat = Employee()
dipu = Employee()

samrat.name = "Samrat"
samrat.salary = 1000000
samrat.role = "CEO"

dipu.name = "Dipesh"
dipu.salary = 5000
dipu.role = "Coordinator"

print(samrat.printdetails())
print()
print(dipu.printdetails())
#print(samrat.name)