# Types of Methods

class Student:
    school = "Assassination"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Instance variables
    def get_m1(self):  # Accessors
        return self.m1

    def set_m1(self, value):  # Mutator
        self.m1 = value

    # Class Methods
    @classmethod
    def get_school(cls):
        return cls.school

    # Static Methods
    @staticmethod
    def info():  # leave parameter blank.. no self or cls
        print("This is classroom")


s1 = Student(50, 60, 70)
s2 = Student(55, 65, 75)
print(s1.avg())
print(s2.avg())
print(Student.get_school())

Student.info()
