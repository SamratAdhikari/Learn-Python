
# Constructor, Self and Compairing Objects

class Computer:
    def __init__(self):
        self.name = "Samrat"
        self.age = 18
 #   def update(self):
 #       self.age = 69

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

com1 = Computer()
com2 = Computer()

com1.name = "Anonymous"
com1.age = 17

#com1.update()
if com1.compare(com2):
    print("They are same.")
else:
    print("They are different.")

print(com1.name)
print(com2.name)

print(com1.age)
