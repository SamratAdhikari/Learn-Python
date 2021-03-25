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
            
            """


)


Contact = {
    "SAMRAT":["9825108250", "samratmetaladhikari@gimal.com"],
    "BABA":["9846031006", "adhikarilal@gmail.com"],
    "MOM":["9846100858", "netramayaadhikari@gmail.com"],
    "ASMITA":["9815176629", "asmitaadhikari@gmail.com"]
   }
name = input("Enter Contact Name: ").upper()

print(Contact["SAMRAT"])
print(
    """
    
    """)
print ("Showing details of %s ::" % (name.capitalize()))
print(

    """
    """)
print("Contact Number: %s" %(Contact[name][0]))
print("Gmail Id: %s" % (Contact[name][1]))

print(

    """
    
    """)

ask = input("""This window will exit.
Press anything and hit Enter......""")






















