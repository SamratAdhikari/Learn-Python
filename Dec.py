""""
def func1():
    print("Hello!!")


func2 = func1
del func1
func2()


def fuc(num):
    if num == 0:
        return print
    if num == 1:
        return sum
a = fuc(1)
#print(a)




def executor(fuc):
    fuc("this")
executor(print)
"""

def dec1(func3):
    def nowexec():
        print("Executing")
        func3()
        print("Executed")

    return nowexec
@dec1
def func3():
    print("My name is Samrat")
#hey = dec1(hey)
func3()
