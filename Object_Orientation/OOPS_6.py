
# Inner Class

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand = "Acer"
            self.cpu = "i5"
            self.ram = "'8GB"

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 =Student("Samrat", 32)
s2 =Student("Shraddha", 18)

print(s1.name, s1.roll)
print(s2.name, s2.roll)
print()

s1.show()

lap1 = Student.laptop()
lap2 = s2.lap
