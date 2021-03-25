
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

    #email change garera diyo bhane 1st name ra last name aafai change garni function...

    @email.setter
    def email(self, string):

        print("Setting Now!!!")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    #to delete email
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

Nepal = Employee("Samrat", "Adhikari",)
Gorkha = Employee("Guru", "Gorkhali")

Gorkha.fname = "BackOff"
Gorkha.lname = "India"
print(Nepal.explain())

print(Gorkha.email)

print(Gorkha.lname)
print(Gorkha.fname)

del Gorkha.email
print(Gorkha.email)
print(Gorkha.fname)


Gorkha.email = "New.Email@gmail.com"
print(Gorkha.email)
