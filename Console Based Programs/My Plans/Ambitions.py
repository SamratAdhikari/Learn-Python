print("""

\t \t \t \t \t \t \t My Plans for my Company !!!



""")


def getdate():
    import datetime
    return datetime.datetime.now()


def amb():
    ask0 = str(input("Enter 'log' to edit and 'read' to retrieve the file:  "))
    print("")
    if ask0 == "log":
        print("")
        ask = str(input("Enter the Plan: "))
        print("")
        ask1 = str(input("Write the description about the plan: "))
        print("")
        ask2 = str(input("How you came up with this idea: "))
        print("\n")
        f = open("Plans_Projects.txt", "a")
        a = f.write(f"[ {getdate()} ] : {ask} \n \t -- {ask1} \n \t \t({ask2})")
        f.close()

        print("Done")
        input("Press Enter to exit...")
    elif ask0 == "read":
        f = open("Plans_Projects.txt")
        a = f.read()
        print(a)
        f.close()
        input("Press Enter to exit...")


amb()
