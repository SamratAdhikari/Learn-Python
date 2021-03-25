
# Astrologer's Stars


def astro_main():
    ask1 = int(input("How many rows do you wanna print? "))
    ask2 = int(input("Type 1 or 0: "))
    if ask2 == True:
        for i in range(ask1 +1):
            print("*  " *int(i))

    elif ask2 == False:
        for i in range(ask1 ,0 ,-1):
            print("* " * int(i))

def astro_play():
    yes_list = ["yes", "y", "YES", "Y", "Yes"]
    astro_main()
    ask_play = input("Do you wanna run the program again? ")
    if ask_play in yes_list:
        astro_play()
    else:
        print("This program is exiting...")
astro_play()
