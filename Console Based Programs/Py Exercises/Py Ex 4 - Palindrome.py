# The Next Palindrome
''''
Author : Samrat Adhikari
Date : 06 June 2020
Purpose : Practice
'''
def is_pal(ask_run):
    return str(ask_run) == str(ask_run)[::-1]

def next_pal(ask_run):
    while not is_pal(ask_run):
        ask_run += 1
    return ask_run
def pal_main():
    numbers = []
    no = int(input("Enter the no of times you wanna run the program: "))
    print()

    for i in range(no):
        ask_n = int(input("Enter any number: "))
        numbers.append(ask_n)
    print()
    for i in range(no):
        print(f"Next palindrome for {numbers[i]} is {next_pal(numbers[i])}")

def pal_play():
    print()
    pal_main()
    print()
    ask_play = str(input("Run the program again?(y/n) "))
    if ask_play == "y":
        pal_play()
    else:
        print("This program is exiting...")
pal_play()

# print(pal_main.__doc__)
