

# def name(a, b, c, d):
#     print(a, b, c, d)
# name("Samrat", "Nissan", "Dipesh", "Bidhan", "Bigyan")


def fun(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    print("\nNow Let me introduce you to someone:")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")



sam = ["Samrat", "Nissan", "Dipesh", "Bidhan", "Bigyan"]
normal = "I am a Normal Argument." \
         "The Students are:"
kw = {"Samrat":"LW",
      "Nissan":"CMD",
      "Bidhan":"CF",
      "Dipesh":"GK",
      "Bigyan":"LCD"}
fun(normal, *sam, **kw)


def new(normal, *args, **kwargs):
    print(normal)
    #print(args)
    for key, value in kwargs.items():
        print(f"{key} is {value}")


   # print(kwargs)
#new("Samrat", 18, "Pokhara", 9825108250) """for args"""
new("Dipesh", age = 17, city = "Pokhara", phn = 9876543210) #for kwargs






