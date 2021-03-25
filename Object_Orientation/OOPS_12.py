# Polymorphism:
# - Duck Typing
# - Operator Overloading
# - Method Overloading
# - Method Overriding

#Method Overriding ---------------

class A:
    def show(self):
        print("Father's Bike - Honda")
# I aint got no bike with me now, so if someone asks me if I have a bike, I can simply say that i do and its Honda
# cause my father has a bike... i inherited by father's bike.

class B(A):
    def show(self):
        print("My Bike - Pulsar")
# Since i have got my own bike and someone asks me which bike i have, I can say its Pulsar... I wont say its Honda
#  cause I have got my own bike now ... i dont need to use by father's character(properties) anymore...


a1 = B()
a1.show()