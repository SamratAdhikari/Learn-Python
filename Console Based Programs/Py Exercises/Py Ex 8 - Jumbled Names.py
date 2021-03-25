import random

namey = []
listey = []
size = int(input("friends: "))
for i in range(size):
    name = input("name: ")
    name1 = name.split(" ")
    listey.append(name1)
    print(listey)

for i in range(size):
    a = random.choice(listey)
    c = random.choice(listey)
    # print(f"[{a}, {c}]")
    print("---------------")
    if f"[{a}, {c}]" not in listey:
        b = a[0].capitalize() + " " + c[1].capitalize()
        # namey.append(b)
        print(b)
        # print(f"{a} {c}")
    # print(namey[i])
#
# # [['aa', 'bb'], ['aa', 'bb']]

# print("-------------------")
