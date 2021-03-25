

class Employee:
    no_of_leaves = 10
    pass

samrat = Employee()
dipesh = Employee()
nishan = Employee()

samrat.name = "Samrat"
dipesh.name = "Dipesh"
nishan.name = "Nishan"

samrat.salary =1000
dipesh.salary =500
nishan.salary =100

samrat.role = "Programmer"
dipesh.role = "Student"
nishan.role = "Teacher"

print(samrat.name)
print(dipesh.name)
print(nishan.name)
print()

print(samrat.no_of_leaves)
print(dipesh.no_of_leaves)
print(Employee.no_of_leaves)
print()

Employee.no_of_leaves = 15
print(Employee.no_of_leaves)
print(samrat.no_of_leaves)
samrat.no_of_leaves = 20
print(samrat.no_of_leaves)
print()

print(samrat.__dict__)
samrat.no_of_leaves = 25
print(samrat.no_of_leaves)
