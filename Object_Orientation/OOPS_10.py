# Polymorphism:
# - Duck Typing
# - Operator Overloading
# - Method Overloading
# - Method Overriding

# Operator Overloading ----------

class Students:
    def __init__(self, m1, m2):
        self.m2 = m2
        self.m1 = m1

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m = Students(m1, m2)
        return m
    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        if m1>m2:
            return True
        else:
            return False
    def __str__(self):
        return "{}, {}".format(self.m1, self.m2)

m1 = Students(15, 65)
m2 = Students(10, 75)

m = m1 + m2
print(m.m2)
print(m1)
print(m2)

print()

if m1>m2:
    print("m1")
else:
    print("m2")