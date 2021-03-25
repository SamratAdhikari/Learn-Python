
s = 7 # This is Global variable
        #  Function bhitra ko lai local ani bahira bhako lai global

def sam():
  #  s = 45 <=========:
    #         This is Local variable. local variable lai change garna milxa...
    #         But function bhitrai tyo variable xa bhane matra...
    #         IF local variable xaina bhane yetikkai function bhitra global variable lai
    #         change garna mildaina....
    #         change garna xa bhane tyo function bhitra 'global s' lekhnu parxa

    global s
    s = s + 1
    print(s)

sam()


x = 89
def sam1():
    # global x
    x = 20
    def sam2():
        global x
        x = 88
        print("before calling sam2", x)
    sam2()
    print("after calling sam2", x)
sam1()
print(x)



v = 10
print(v)

def again():
    v = 9
    g =globals()["v"]
    print("in fun", v)
    globals()["v"] = 15

again()
print("outside", v)




