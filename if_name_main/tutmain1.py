
def sam(ask1):
    return f"hello {ask1}"

def addnum(ask01, ask02):
    return ask01+ask02


print("the module/function is ", __name__)
if __name__ == '__main__':
    print(sam("Samrat"))
    print(addnum(2, 6))
