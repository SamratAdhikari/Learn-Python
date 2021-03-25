# Fraud Multiplication Table

import random

def fakeMulti(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table


def correctMulti(table, number):
    for i in range(1, 11):
        if table[i - 1] != i * number:
            return i - 1
    return None


if __name__ == '__main__':
    # print(fakeMulti(7))
    number = int(input("Enter any number: "))
    myTable = fakeMulti(number)
    print(myTable)
    wrongIndex = correctMulti(myTable, number)
    print(f"The table is wrong at {wrongIndex + 1} number.")
