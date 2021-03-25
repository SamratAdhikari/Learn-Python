#  Fuction banauna jhyau layo bhane lambda use garni

minus = lambda x, y: x-y


add = lambda x, y: x + y

print(minus(1, 2))
print(add(1, 3))

# list_first lambda

lis = [[1, 14], [11, 6], [9, 0]]

lis.sort(key = lambda x: x[1])
print(lis)

lis.sort(key = lambda x: x[0])
print(lis)
