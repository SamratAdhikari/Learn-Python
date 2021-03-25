# Palindromify the list

def pal_next(ask2):
    ask2 += 1
    while not pal_str(ask2):
        ask2 += 1
    return ask2


def pal_str(ask2):
    ask = str(ask2)
    return ask == ask[::-1]


def palist_main():
    my_list = []
    list_out = []
    ask1 = int(input("How many numbers to you wanna process? "))
    for i in range(ask1):
        ask2 = int(input("Enter any number: "))
        my_list.append(ask2)
    print(f"Your list is {my_list}")

    for element in my_list:
        if element > 10:
            n = pal_next(element)
            list_out.append(n)

        else:
            list_out.append(element)

    print(f"Your output list is {list_out}")


        # for i in range(ask1):
        #     if ask2 >= 10:
        #         list_out.append(pal_next(ask2))
        #
        #     else:
        #         list_out.append(i)
        #
        # list_out.sort()
        # print(list_out)
        #

def palist_play():
    palist_main()
    ask_play = str(input("Run the progarm again?(y/n) "))
    if ask_play == "y":
        palist_play()
    else:
        print("This program is exiting...")


palist_play()
