from time import sleep

print("""
                         Welcome to my calculator...

      """)


def area_calc():
    print(

        """
        This is a area calculator...

        """)

    option = input("""Enter: 
               C for Circle    
               T for Triangle  
               R for Rectangle 
               S for Square   

               Choice : """)
    option = option.upper()

    if option == "C":
        print("Calculation of area of Circle")
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * (radius ** 2)

        print(f"The area of your circle is {area} m")



    elif option == "T":
        print("Calculation of area of Triangle")
        le = float(input("Enter length: "))
        br = float(input("Enter breadth: "))
        area1 = 0.5 * le * br
        print("The area of your triangle is %s" % (area1))


    elif option == "R":
        print("Calculation of area of Rectangle")
        le = float(input("Enter length: "))
        br = float(input("Enter breadth: "))
        area2 = le * br
        print("The area of your rectangle is %s" % (area2))

    elif option == "S":
        print("Calculation of area of Square")
        le = float(input("Enter length: "))
        area3 = le ** 2
        print("The area of your rectangle is %s" % (area3))


    else:
        print("You moron...")


def simple_calc():
    print("""
    This is a Simple Calculator...

    """)

    option = input("""
                Enter:
                A for Addition
                S for Subtraction
                M for Multiplication
                D for Division

                Choice : """)
    option = option.upper()

    if option == "A":
        print("""
            Now performing Addition...
            Please type in the numbers for the calculation.
            Type '0' & Press 'Enter', if there are no further numbers to add.

            """)
        a = int(input("Enter first number : "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number : "))
        d = int(input("Enter forth number : "))
        e = int(input("Enter fifth number : "))
        print("Calculating")

        sleep(1)
        add = a + b + c + d + e

        print('The Answer is: ', add)

    if option == "S":
        print("""
                   Now performing subtraction...
                   Please type in the numbers for the calculation.
                   Type '0' & Press 'Enter', if there are no further numbers to subtract.

                   """)
        a = int(input("Enter first number : "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number : "))
        d = int(input("Enter forth number : "))
        e = int(input("Enter fifth number : "))
        print("Calculating")

        sleep(1)
        sub = a - b - c - d - e

        print('The Answer is: ', sub)

    if option == "M":
        print("""
                   Now performing Multiplication...
                   Please type in the numbers for the calculation.
                   Type '1' & Press 'Enter', if there are no further numbers to multiply.

                   """)
        a = int(input("Enter first number : "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number : "))
        d = int(input("Enter forth number : "))
        e = int(input("Enter fifth number : "))
        print("Calculating")

        sleep(1)
        mul = a * b * c * d * e

        print('The Answer is: ', mul)

    if option == "D":
        print("""
                   Now performing Division...
                   Please type in the numbers for the calculation.
                   Type '1' & Press 'Enter', if there are no further numbers to divide.

                   """)
        a = int(input("Enter first number : "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number : "))
        d = int(input("Enter forth number : "))
        e = int(input("Enter fifth number : "))
        print("Calculating")

        sleep(1)
        div = a / b / c / d / e

        print('The Answer is: ', div)


def play_calc():
    opt = input("""

                What would you like to calculate?
                A. Simple Calculator
                B. Area Calculator
                C. Perimeter Calculator
                D. Trigonometric Calculator

                Choice : """)
    opt = opt.upper()
    yes_list = ["yes", "YES", "Yes", "Y", "y"]
    if opt == "A":
        simple_calc()
        ask = input("\nRun the program again?")
        if ask in yes_list:
            play_calc()
    elif opt == "B":
        area_calc()
        ask = input("\nRun the program again?")
        if ask in yes_list:
            play_calc()
    else:
        print(input("\nPress any key to Exit..."))


play_calc()

