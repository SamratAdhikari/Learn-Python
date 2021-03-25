

s = open("samrat.txt")
print(s.read())

print(s.readline())
# print(s.tell())
print(s.readline())


s.seek(0)
print(s.readline())


s.close()