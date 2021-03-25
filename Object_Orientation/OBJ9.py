class A:
    classvar = "I am in class A"
    def __init__(self):
        self.varl = "I am inside class A's constructor"
        self.classvar1 = "Insatance var in class A"
        self.special = "This is special A"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.varl = "I am inside class B's constructor"
        self.classvar1 = "Insatance var in class B"

a = A()
b = B()


print(b.special, b.varl, b.classvar1)