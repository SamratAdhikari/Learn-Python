# Inheritance
# => Single, Multilevel and Multiple

class A: # "Grandfather"
    def feature1(self):
        print("Feature 1 working...")

    def feature2(self):
        print("Feature 2 working...")

class B(A): # B is child class(sub class) of A  # Father
    def feature3(self):
        print("Feature 3 working...")

    def feature4(self):
        print("Feature 4 working...")

class C(B): # Son # C is child class of B
    def feature5(self):
        print("Feature 5 working...")

# if class B aint inheriting from class A:
#class C(A, B): #we can assign class C with A and B's funtions(methods)
# ....
a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature1() # b1 can access class A
b1.feature3() # b1 can access its own class

c1 = C()

c1.feature1() # c1 can access class A
c1.feature4() # c1 can access class B
c1.feature5() # c1 can access its own class C