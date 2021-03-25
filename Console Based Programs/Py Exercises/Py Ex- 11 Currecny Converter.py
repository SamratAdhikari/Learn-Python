# Currency Converter

with open("Currency.txt") as f:
    lines = f.readlines()

currentDict = {}
for line in lines:
    parsed = line.split("\t")
    currentDict[parsed[0]] = parsed[1]

# print(currentDict)
print("Avaliable options:")
[print (item) for item in currentDict.keys()]
amount = int(input("Enter the amount: "))
currency = input("Enter the name of currency to convert into: ")

print()
print(f"Rs. {amount} = {amount * float(currentDict[currency])} {currency}")
