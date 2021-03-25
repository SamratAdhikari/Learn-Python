# Polymorphism:
# - Duck Typing
# - Operator Overloading
# - Method Overloading
# - Method Overriding

# Duck Typing-------------

class PyCharm:
    def execute(self):
        print("Compiling...")
        print("Running...")

class MyEditor:
    def execute(self):
        print("Spell Checking")
        print("Convention Check")
        print("Compiling...")
        print("Running...")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

