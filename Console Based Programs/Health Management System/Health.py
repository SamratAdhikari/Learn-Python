# Health Management System

print("""

               Client Names:
               
                       Nissan
                       Dipesh
                       Bidhan
                       Bigyan
                       Samrat
""")

def getdate():
    import datetime
    return datetime.datetime.now()


def main():
    ask = input("Enter Client Name: ")
    ask = ask.upper()
    print(ask)
    if ask == "NISSAN":

        ask1 = input("Enter 'Diet' or 'Exercise' to execute : ")
        ask1 = ask1.lower()
        if ask1 == "diet":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Diet: ")
                with open("Nissan_diet.txt", "a") as d:
                    a = d.write("[ " + str(getdate()) + " ]" +" "+ ask2)
                    a = d.write("\n")
                    print("[", str(getdate()), "]", ask2)
            else:
                d = open("Nissan_diet.txt")
                print(d.read())


        elif ask1 == "exercise":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Exercise: ")
                with open("Nissan_ex.txt", "a") as e:
                    a = e.write("[ " + str(getdate()) + " ]" + " " + ask2)
                    a = e.write("\n")
                    print("[", str(getdate()), "]", ask2)
            else:
                d = open("Nissan_ex.txt")
                print(d.read())



    elif ask == "BIDHAN":
        ask1 = input("Enter 'Diet' or 'Exercise' to execute : ")
        ask1 = ask1.lower()
        if ask1 == "diet":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Diet: ")
                with open("Bidhan_diet.txt", "a") as d:
                    a = d.write("[ " + str(getdate()) + " ]" + " " + ask2)
                    a = d.write("\n")
                    print("[", str(getdate()), "]", ask2)
            else:
                d = open("Bidhan_diet.txt")
                print(d.read())


        elif ask1 == "exercise":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Exercise: ")
                with open("Bidhan_ex.txt", "a") as e:
                    a = e.write("[ " + str(getdate()) + " ]" + " " + ask2)
                    a = e.write("\n")
                    print("[", str(getdate()), "]", ask2)
            else:
                d = open("Bidhan_ex.txt")
                print(d.read())

    elif ask == "DIPESH":
        ask1 = input("Enter 'Diet' or 'Exercise' to execute : ")
        ask1 = ask1.lower()

        if ask1 == "diet":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Diet: ")
                with open("Dipesh_diet.txt", "a") as d:
                    a = d.write("[ " + str(getdate()) + " ]" +" "+ ask2)
                    a = d.write("\n")
                    print("[", str(getdate()), "]", ask2)

            else:
                d = open("Dipesh_diet.txt")
                print(d.read())

        elif ask1 == "exercise":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Exercise: ")
                with open("Dipesh_ex.txt", "a") as e:
                    a = e.write("[ " + str(getdate()) + " ]" + " " + ask2)
                    a = e.write("\n")
                    print("[", str(getdate()), "]", ask2)

            else:
                d = open("Dipesh_ex.txt")
                print(d.read())

    elif ask == "BIGYAN":
        ask1 = input("Enter 'Diet' or 'Exercise' to execute : ")
        ask1 = ask1.lower()
        if ask1 == "diet":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Diet: ")
                with open("Bigyan_diet.txt", "a") as d:
                    a = d.write("[ " + str(getdate()) + " ]" + " " + ask2)
                    a = d.write("\n")
                    print("[", str(getdate()), "]", ask2)
            else:
                d = open("Bigyan_diet.txt")
                print(d.read())


        elif ask1 == "exercise":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Exercise: ")
                with open("Bigyan_ex.txt", "a") as e:
                    a = e.write("[ " + str(getdate()) + " ]" + " " + ask2)
                    a = e.write("\n")
                    print("[", str(getdate()), "]", ask2)
            else:
                d = open("Bigyan_ex.txt")
                print(d.read())

    elif ask == "SAMRAT":
        ask1 = input("Enter 'Diet' or 'Exercise' to execute : ")
        ask1 = ask1.lower()
        if ask1 == "diet":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Diet: ")
                with open("Samrat_diet.txt", "a") as d:
                    a = d.write("[ " + str(getdate()) + " ]" + " " + ask2)
                    a = d.write("\n")
                    print("[", str(getdate()), "]", ask2)
            else:
                d = open("Samrat_diet.txt")
                print(d.read())


        elif ask1 == "exercise":
            ask0 = input("Enter 'log' to edit or 'read' to retrive the file: ")
            if ask0 == "log":
                ask2 = input("Enter the Exercise: ")
                with open("Samrat_ex.txt", "a") as e:
                    a = e.write("[ " + str(getdate()) + " ]" + " " + ask2)
                    a = e.write("\n")
                    print("[", str(getdate()), "]", ask2)
            else:
                d = open("Samrat_ex.txt")
                print(d.read())

    else:
        print("Try Again!!!")

    print("\n")
    hey = input("Run the program ?? (y/n) :")
    if hey == "y":
      print("\n")
      main()
    else:
        exit()
print("\n")
main()












