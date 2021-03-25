# Array values from user

from array import *

arr = array("i", [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    user = int(input("Enter the value: "))
    arr.append(user)

print(arr)

check = int(input("Enter he value for search: "))
a = 0
for i in arr:
    if i == check:
        print(f"Yes, {check} is in the array in position {a+1}.")
        break

    a += 1

# Shortcut using inbuilt func
print(arr.index(check))