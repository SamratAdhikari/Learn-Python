# Comprehensions.............


# List-------------
# multi3 = []
# for i in range(100):
#    if i%3 == 0:
#        multi3.append(i)


# --- Shortcut Method

# list Comprehensions
multi3 = [i for i in range(1, 100) if i % 3 == 0]
print(multi3)
print()

# Dictionary----------

# dict1 = {0:"item0", 1:"item1" ..... and so on}

# Dictionary Comprehensions
dict1 = {i: f"Item{i}" for i in range(1, 100) if i % 3 == 0}
# To reverse the dictionary:
dict1 = {value: key for key, value in dict1.items()}
print(dict1)
print()

# Sets Comprehensions

dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2"]}

print(dresses)
print()

# Generator Comprehenions

gen = (i for i in range(100) if i%2 == 0)
for i in gen:
    print(i)