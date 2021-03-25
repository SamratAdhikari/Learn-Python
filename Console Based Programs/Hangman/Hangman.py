# Hangman

# title
print()
print("Welcome to Hangman Game".center(100))
print()

# modules
from random import *


# Rules
if input("Do you want to read the Instructions?(y/n) \n") == "y":
    print("Instructions:\n"
          "\tYour friend Samrat is about to be hanged...\n"
          "\tA word is given in the form of silhouette...\n"
          "\tYou need to guess the word within 6 chances to save him...\n"
          "\tYou can guess the word in a single go...\n"
          "\tOr you could play safe and guess the letters individually...\n"
          "\tIf you guess a wrong letter/word, your chance(s) will be reduced...\n"
          "\tGuess the word and you can save your buddy !")
    input("Press Enter to Play The Game !!!")
    # sleep(7)
print("------------------------------------")
print()


def word_list():
    listey = []
    wlist = []
    slist = []
    with open("wordlist.txt") as f:
        for line in f:
            up_line = line.strip().upper()
            listey.append(up_line)
    ask_level = str(input("Enter the level of game - [E]asy or [H]ard:\n").upper())
    print()
    if ask_level == "E":
        listey_easy = []
        for item in listey:
            if len(item) <= 5:
                listey_easy.append(item)
        print("Game Level: Easy")
        word = choice(listey_easy)

    elif ask_level == "H":
        listey_hard = []
        for item in listey:
            if len(item) > 5:
                listey_hard.append(item)
        print("Game Level: Hard")
        word = choice(listey_hard)

    else:
        print("Invalid Input !!!")
        word_list()

    for i in word:
        # word list
        wlist.append(i)
        # silhouette
        slist.append("_")
    main(slist, wlist)


# words gen and checker
def main(slist, wlist):
    # print(wlist)
    chances = 6
    # display the silhouette of the gen word
    num = 0
    for i in wlist:
        num += 1
    print(f"There are {num} letters in the generated word!")

    # used letters
    alist = set()


    # for while
    end = False
    
    while chances != 0 and not end:
        print()
        if chances == 0:
            print("\nGame Over...\nYour friend was Hanged!!!")
            show = "".join(wlist)
            print(f"The word is {show}")
            end = True
            
        print(' '.join(slist))
        # print used letters
        print(f"Used Letters: {' '.join(alist)}")
        # ask user for input
        ask = str(input("Enter a letter: ")).strip().upper()

        # conditions
        if ask == "".join(wlist):
            print("Congrats! You guessed the word...")
            break

        elif ask in wlist:
            #print("elif ask in wlist")
            if ask in alist:
                #print("if ask in alist")
                print("You used the letter before...")
                chances -= 1
                print(f"Chances left: {chances}")

            elif ask not in alist:
                #print("elif ask not in alist")
                print("Correct!!!")
                for index, item in enumerate(wlist):
                    if ask == item:
                        slist[index] = wlist[index]
                    if slist == wlist:
                        print("Congrats! You guessed the word...")
                        end = True
                alist.add(ask)

        elif ask not in wlist:
            #print("elif ask in wlist")
            if ask in alist:
                #print("if ask in alist")
                print("You used the letter before...")
            elif ask not in alist:
                print("Sorry!!!")
                alist.add(ask)
                
            chances -= 1
            print(f"Chances left: {chances}")
            # print()

def run():
    word_list()  
    if str(input("Run the program again? (y/n) ")) == "y":
        run()  
run()
    

