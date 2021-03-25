#






## Map------------------------------------------------------------------------------------------




numbers = ["7", "10", "11", "1", "4"]
numbers = list(map(int, numbers))
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers[2] = numbers[2] + 1
print(numbers[2])
sq = lambda x: x*x
num = [2, 3, 5, 9, 5, 55, 21, 45]
square = list(map(sq, num))
print(square)
s = lambda x: x**2
c = lambda x: x**3
fun = [s, c]
for item in range(5):
    val = list(map(lambda x: x(item), fun))
    print(val)
#
#

# Filter------------------------------------------------------------------------------------------
list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_greater(num):
    return num > 5
#
gr_than_5 = list(filter(is_greater, list_1))
print(gr_than_5)





# Reduce------------------------------------------------------------------------------------------

from functools import reduce
list_2 = [1, 2, 3, 4, 5]
# num = 0
# for i in list_2:
#     num = num + i
# print(num)

num1 = reduce(lambda x,y: x+y, list_2)
print(num1)



