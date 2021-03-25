n = int(input("Enter number: "))

def factorial_iterative(n):
    a = 1
    for i in range(n):
        a = a * (i+1)
    return a
print("Factorial using iterative method:", factorial_iterative(n))


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print("Factorial using recursive method:", factorial_recursive(n))


