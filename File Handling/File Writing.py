# f = open("samrat.txt", "w")
# f.write("Samrat is awesome. \n"
#         "He is cool. \n"
#         "He loves football. \n")


# f = open("samrat.txt", "a")
# a = f.write("Samrat says Hi !!")
# print(a) # print(a) garyo bhane tya lekheko kati ota characters xa, tyo bhanxa...

f = open("samrat.txt", "r+")
print(f.read())
f.write("Thank you...")


f.close()


