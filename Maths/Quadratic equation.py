import cmath
from time import sleep
# Importing Complex Maths

print("\t\t\tThe Syantax for the quadratic equation should be: \nax^2 + bx + c = 0")
def quad1():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    d = ((b**2) - (4*a*c))

    sol1 = (- b - cmath.sqrt(d))/(2*a)
    sol2 = (- b + cmath.sqrt(d))/(2*a)
    sleep(1)
    print(f"The solutions of given quadratic equation are: \t{sol1} and \t{sol2}")

quad1()

