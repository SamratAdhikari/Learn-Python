from random import randint
def guess_num():
    n = randint(1, 100)
   # print(n)
    for i in range(10):
        ask = int(input("Enter any number from 1-100: "))
        if ask == n:
            print(f"Congrats! {n} is the correct answer.")
            print(f"You guessed the no. correctly in {i+1}th iteration.")
            break
        elif n > ask:
            if (n - 10) >= ask:
                print("Your guess is much lower than the actual number.")
            else:
                print("Your guess is lower than the actual number.")

        elif n < ask:
            if (n + 10) <= ask:
                print("Your guess is much higher than the actual number.")
            else:
                print("Your guess is higher than the actual number.")
        elif ask < 1 or ask > 100:
            print("Invalid")
        

def play_RPS():
    guess_num()
    ask_play = input("\nDo you wanna run the program again?? ")
    yes_list = ["yes", "y", "YES", "Y", "Yes"]
    if ask_play in yes_list:
        play_RPS()
    else:
        print("The program is exiting...")
play_RPS()


