
print("\n"
      "-------------------------------Permutation-----------------------------"
      "\n")
import math
import builtins
#P(n,r)

def permute():

    ask = input("Linear Permutation (l) \n"
                "Circular Permutation (c) \n"
                "Letter Permutation (w) \n"
                "Choice : ")
    if ask == "l":

        try:
            n = int(input("Enter number of distinct objects(n): "))
            r = int(input("Enter number of distinct objects taken at a time (r): "))
            solve = (math.factorial(n)) / (math.factorial(n - r))
            print(f"\nThe Selecting Ways are {solve}.")
        except Exception as e:
            print(e)

    elif ask == "c":

        try:
            n = int(input("Enter the number (n): "))
            solve = (math.factorial(n - 1))
            print(f"\nThe Selecting Ways are {solve}.")
        except Exception as e:
            print(e)
    elif ask == "w":
        try:
            n = input("Enter any Word: ")
            letters = {}
            for c in n:
                if c not in letters:
                    letters[c] = 1
                else:
                    letters[c] += 1
            for i in letters[1]:
                if letters[1] >= 2:
                    p = letters[1]
            solve = math.factorial(len(n))/(math.factorial(p))

            print()



            solve = (math.factorial(n))/((math.factorial(p))*(math.factorial(q)*math.factorial(r)))
               # print(i, end = " ")
        except Exception as e:
            print(e)
permute()
