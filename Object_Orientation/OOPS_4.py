
# Types of Variables
# => Instance Variables and Class Variables
class Car:
    wheels = 4 # Class variables
    def __init__(self):
        self.mileage = 10               # Instance Variables
        self.company = "Lamborghini"     # Instance Variables

c1 = Car()
c2 = Car()

Car.wheels = 5
Car.mileage = 11 # init bhitra bhayera c1 ra c2 ko change hunna tara Car itself ko chai change hunxa...

print(c1.company, c2.mileage)
print(c2.company, c1.mileage)
print(c1.wheels)

