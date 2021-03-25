import sympy as sp
from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt

#Given Function: f(x) = 3*x**2 + 4*x
print("\t\t\t f(x) = 6*x**3 + 4*x**2 + 3*x + 2\n")
#ask = str(3*x**2 + 4*x)
sadasdasdasdasdsadsadasddddddddddddddddd
# Derivation
x = sp.Symbol("x")
ans1 = sp.diff(7*x**3 + 6*x, x)
print(f"The First derivative of the given function is {ans1}\n")

## Max value (Maxima)

def f(x):
    return 6*x**3 + 4*x**2 + 3*x + 2
ans2 = derivative(f, 2)
print(f"The maximum value of the given function is {ans2}\n")

### Graphical representation of f(x)

y = np.linspace(-3,3)
plt.plot(y,f(y))
plt.show()




