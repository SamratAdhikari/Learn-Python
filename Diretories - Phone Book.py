print(""" 

            ----------- PHONE BOOK ------------ 
                
                     """)
print(
    """
                 Name List
        
                Samrat
                Baba
                Mom
                Asmita
                Samjhana
            """

)


def contact1():
    Contact = {
        "SAMRAT": ["9825108250", "samratmetaladhikari@gmail.com"],
        "BABA": ["9846031006", "adhikari123lal@gmail.com"],
        "MOM": ["9846100858", "netramayaadhikari@gmail.com"],
        "ASMITA": ["9814131860", "asmitaadhikari@gmail.com"],
        "SAMJHANA": ["9815176629", "samjhanaadhikari128@gmail.com"]
    }
    name = input("Enter Contact Name: ")
    name = name.upper()
    name1 = name.lower()

    for i in name:
        a = name[0]
        d = name1[1:len(name1) + 1]
        name2 = a + d

        print(

            """
            
            """)
        print("Showing details of %s ::" % (name2))
        print(

            """
            """)
        print("Contact Number: %s" % (Contact[name][0]))
        print("Gmail Id: %s" % (Contact[name][1]))
        print("\n")

    hey = input("Run Program again?(y/n) : ")
    if hey == "y":
        print("\n")
        contact1()

    else:
        exit()


contact1()
