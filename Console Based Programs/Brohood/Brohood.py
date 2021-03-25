print(
    """
                       Here is the list of my brothers along with me.

                                    Samrat 
                                    Nissan
                                    Dipesh
                                    Bigyan
                                    Bidhan


    This program will ask you to write a name from the above list.
    and it will print the number in which the person lies according to age...

    And again it will ask you  to type the number and it will print the name according to the age....

    So literally, if the person whose "name" you entered is the eldest of all, it will print number "1" 
    and vice-versa ,if you entered the number

"""
)






def Brohood_string(Name):
    return {
        "Nissan" : 1,
        "Bigyan" : 2,
        "Samrat" : 3,
        "Bidhan" : 4,
        "Dipesh" : 5
        }[Name]
"""  




"""    
sm = input("Enter name: ")
sm = sm.lower()
for i in sm :
    a = sm[0]
    a = a.upper()
    b = sm[1: len(sm)+1]
    sam = a + b 

print(
    Brohood_string(sam) 
)

print("""

"""
)
def Brohood_number(Number):
    return {
        1 : "Nissan",
        2 : "Bigyan",
        3 : "Samrat",
        4 : "Bidhan",
        5 : "Dipesh"
        }[Number]

print("""

""")

mas = input("Enter no: ") 
a = int(mas)
print(Brohood_number(a))



print("""

"""
)

ask = input("""This window will exit.
Press anything and hit Enter......""")
print(ask)












