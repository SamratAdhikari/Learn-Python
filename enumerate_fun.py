

list1 = ["Naruto", "One Piece", "Attack on Titan", "Fullmetal Alchemist", "Dr. Stone", "Death Note"]

for index, item in enumerate(list1):
    if index%2 == 0:
        print(f"The selected anime is {item}")
        index += 1
    #else:
    #    print(item)

