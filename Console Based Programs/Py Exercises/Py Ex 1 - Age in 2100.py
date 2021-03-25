# Your age in 2100


year = 2020
def age_main():
    try:
        ask_user = int(input("Enter your age or DoB: "))
        if ask_user <= 100 and ask_user > 0:
            hun_year = 100 - ask_user
            print(f"You will be 100 yrs old in next {hun_year} years.")

            print()
            ask_opt = int(input("Enter a year and know what your age's gonna be: "))
            ans = ask_opt - (year - ask_user)
            if ans < 0:
                print(f"You wont be born yet in {ask_opt} A.D.")
            else:
                print(f"You are gonna be {ans} yrs old in {ask_opt} A.D.")

        elif ask_user <= 0 or (year - ask_user) < 0:
            print("Dude, you aint born yet!!!")

        else:
            if year - ask_user > 120:
                print("Ok Boomer!!!")

            elif year - ask_user <= 100:
                hun_year_dob = year - ask_user
                hun_year = 100 - hun_year_dob
                print(f"You will be 100 yrs old in next {hun_year} years.")

                print()
                ask_opt = int(input("Enter a year and know what your age's gonna be: "))
                ans = ask_opt - ask_user
                if ans < 0:
                    print(f"You wont be born yet in {ask_opt} A.D.")
                else:
                    print(f"You are gonna be {ans} yrs old in {ask_opt} A.D.")

            else:
                print("Something went wrong...")

    except Exception as e:
        print(e)
        age_play()

def age_play():
    print()
    age_main()
    print()
    ask_play = str(input("Run the program again?(y/n) "))
    if ask_play.isalpha():
        if ask_play == "y":
            age_play()
        elif ask_play == "n":
            print()
            print("This program is exiting...")
    elif ask_play.isnumeric():
        print("Invalid input...")
age_play()
