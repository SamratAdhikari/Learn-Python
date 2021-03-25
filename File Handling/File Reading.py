g = open("samrat.txt")

# content = g.read()

print(g.readlines())



# print(g.readline())
# print(g.readline())
# print(g.readline())


for i in g:
    print(i)
# print(content)

# yo content use garyo bhane tyo file ko elements haru linxa ani paxi chai content feri use garda
# tyo elements haru delete gardinxa

g.close()

