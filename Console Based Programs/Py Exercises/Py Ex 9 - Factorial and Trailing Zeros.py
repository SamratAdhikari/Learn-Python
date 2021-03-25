# Factorial and Trailing Zeros

# Modules
from run_pro import run_pro


# Factorial Func
def fac(ask):
    # factorial
    try:
        if ask == 1 or ask == 0:
            return 1
        else:
            return ask * fac(ask - 1)
    except Exception as e:
        return e


# Zero Trailing
def trail(ask):
    # 100! = 100//5(floor division leaves remainder) +100//5*5 .....until 0
    count = 0
    i = 5
    while ask // i != 0:
        count += int(ask / i)
        i = i*5
    return count


# User Input
def user():
    ask = int(input("Enter a number: "))
    print(f"The Factorial of {ask} is {fac(ask)}")
    print(f"No of Trailing Zeros: {trail(ask)}")


# Run Func
run_pro(user)
