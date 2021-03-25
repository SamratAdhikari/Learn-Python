


dic = {
    "Samrat" : "Burger",
    "Nissan" : "Mo:mo",
    "Dipesh" : "Pizza",
    "Bidhan" : {"B" : "maggie", "D" : "chicken"}}
print(dic["Samrat"])

dic["Bigyan"] = "Junk Food"
dic[420] = "Khana"
print(dic)

exit()
del dic[420]

dic1 = dic.copy()
del dic1["Samrat"]

# dic1.update()
dic1.update({"Spandan":"Toffee"})



print(dic)
print(dic1)



print(dic1.keys())

print(dic.items())








