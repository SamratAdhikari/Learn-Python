"""
Iterable = __iter__() or __getitem__()
Iterator = __next__()
Iteration = For/ While Loops
"""

def gen(n):
    for i in range(n):
        yield i
# yield is used to preserve RAM

g = gen(7)

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())