

grocery = ["Samrat", "Nissan", "Dipesh", "Bigyan", "Bidhan", 7, 10, 1, 4, 11]


print(grocery[7])

a = "samrat"
numbers = [11, 85, 12, 65]
#numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[::-1])

numbers.append(18)
numbers.append(a)

print(numbers)

numbers.insert(1, 3)
print(numbers)


print(numbers.pop())



tp = (1, 2, 3)

a = 1
b = 2

a,b = b,a
print(a,b)