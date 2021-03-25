
from time import sleep
no = 7

for i in range(1, 6):
    g = int(input("Guess a Number: "))
    print("You guessed", str(g))


    if g == no:
        sleep(1)
        print("Congrats, your guess was correct !!!")
        print("You guessed in", str(i), "attempt(s) !!!")
        break

    elif g > no:
        sleep(1)
        if i< 5:
            print("Guess less")
        else:
             print("Sry lad, its game over for you ")

    elif g < no:
        sleep(1)
        if i < 5:
            print("Guess less")
        else:
            print("Sry lad, its game over for you ")



    i = i + 1






