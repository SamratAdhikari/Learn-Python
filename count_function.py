


#Counting Spaces::
string1 = "Hello Word!!".count(' ')
print(string1)
    #Alternatively:
string2 = "Samrat Adhikari is my name."
print("the no of spaces is {}".format(string2.count(" ")))

#Counting Letters::
string3 = "Samrat Adhikari is my name.".count("a")
print(string3)

#Counting Words::
a = 0
string4 = "Hey whats up nibba ? you feeling good ?? "
word = string4.split()
print(word)
print(f"The no of words is {len(word)}" )


#Counting numbers:
list1 = [1, 5, 9, 5, 9, 6, 1]
print(list1.count(5))
