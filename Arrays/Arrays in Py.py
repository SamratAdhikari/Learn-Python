# Arrays
# Arrays are similar to lists but an array consists of only one type of values

from array import *

vals = array('i', [5, 9,12,-7])
print(vals)

vals.reverse()
print(f"after reverse {vals}")

vals.append(-89)
print(f"after append {vals}")

print(vals[0])
print()

newArray = array(vals.typecode, (i*i for i in vals))
for i in newArray:
    print(i)