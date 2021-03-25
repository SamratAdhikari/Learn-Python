

# Method Overloading ---------------

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a = None, b = None, c = None): # Method Overloading...
        if a != None and b != None and c != None:
            s = a+b+c
        elif a != None and b!= None:
            s = a+b
        else:
            s = a
        return s

m1 = Student(15, 65)
print(m1.sum(51))
print(m1.sum(51, 15))