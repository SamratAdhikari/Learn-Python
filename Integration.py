import sympy as sp
x = sp.Symbol("x")
print(sp.integrate(sp.exp(-x)*sp.sin(3*x), x))
print("\n")
from scipy.integrate import quad
import numpy as np
def f(x):
    return 3*x**2 + 2*x + 6
i = quad(f,0,2)
print(i[0])
print(i[1])


def integrand(x):
    return x**2

ans, err = quad(integrand, 0, 1)
print (ans)



