# Object Introspection

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # self.email = f"{fname}metal{lname}@gmail.com"

    def explain(self):
        return f"The name is {self.fname} {self.lname}."

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email aint set...! Plz set it using setter!!!"
        return f"{self.fname}.{self.lname}@gmail.com"

    # email change garera diyo bhane 1st name ra last name aafai change garni function...

    @email.setter
    def email(self, string):
        print("Setting Now!!!")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    # to delete email
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
print(skillf.email)
print(dir(skillf))
print(id(skillf))

print()

import inspect
print(inspect.getmembers(skillf))