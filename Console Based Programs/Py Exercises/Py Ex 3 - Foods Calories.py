# Food and Calories


def res_main():
    res_list = []
    print("Enter the  calories of the food one at a time...")
    print()
    sze = int(input("Enter the no of foods that you want to order: "))
    for i in range(sze):
        ask_cal = int(input("Enter the amount of calories for you food: "))
        res_list.append(ask_cal)
    # print(res_list)
    # arranging the list in ascending order
    res_list.sort()
    print(f"The list of your order is {res_list}")
    print()

    rev = res_list[:]
    rev.reverse()
    print(f"The first reverse is {rev}")
    print()
    # reversing the elements of the list
    res_list_rev = res_list[::-1]
    print(f"The second reverse is {res_list_rev}")
    # --------------------
    # reverse1 = res_list[:]
    # reverse1.reverse()

    res_list_rev_sec = res_list[:]
    n = len(res_list)
    print()
    for i in range(n//2):
        res_list_rev_sec[i], res_list_rev_sec[n - i - 1] = res_list_rev_sec[n -i -1], res_list_rev_sec[i]
    print(f"The third reverse is {res_list_rev_sec}")
    print()

    if rev == res_list_rev == res_list_rev_sec:
        print("All three lists are same...")

def res_play():
    res_main()
    ask_play = str(input("Run the program again?(y/n) "))
    if ask_play == "y":
        res_play()
    else:
        print("This program is exiting...")
res_play()