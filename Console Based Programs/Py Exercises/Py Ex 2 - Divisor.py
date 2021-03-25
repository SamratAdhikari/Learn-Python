# Divisor
def div_main():
    try:
        ask_n = int(input("Enter a number: "))
        ask_mn = int(input("Enter the lower bound: "))
        ask_mx = int(input("Enter the upper bound: "))
        if ask_mn > ask_mx:
            print("The lower bound cant be greater than the upper bound...")
            div_play()
        elif ask_mn == ask_mx:
            print("The lower bound cant be equal to the upper bound...")
            div_play()
        elif ask_n < ask_mn or ask_n < ask_mx:
            print("The given number cant be lower than lower bound or upper bound...")
            div_play()
        else:
            for i in range(ask_mn, ask_mx+1):
                if ask_n%i == 0:
                    print(f" {i} is the divisor of {ask_n}.")
                elif ask_n%i != 0:
                    print(f" {i} is not the divisor of {ask_n}.")
    except Exception as e:
        print(e)
        div_play()


def div_play():
    div_main()
    print()
    try:
        ask_play = str(input("Run the program again?(y/n) "))
        if ask_play == "y":
            print()
            div_play()
            print()
        else:
            print("This program is exiting...")
            exit()
    except ValueError:
        print("Invalid input! Enter a string...")
div_play()