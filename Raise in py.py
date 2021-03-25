# Raise

a = input("Enter your name: ")
b = input("Your Earning: ")
if int(b) == 0:
    raise ZeroDivisionError("b is 0 so stopping the program.")
if a.isnumeric():
    raise Exception("Numbers are not allowed.")
else:
    print(f"Hello {a}")
print()

c = input("enter: ")
try:
    print(d)
except Exception as e:
    if c == "samrat":
        raise ValueError("Samrat is blocked")

    print("Exception handled")

