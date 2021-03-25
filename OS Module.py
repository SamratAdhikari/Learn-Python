import os

a = str(__file__)
b = a.replace("/OS Module.py", "")
c = b.replace("/", "\\")
print(c)




# current working dir if the extra file i am using aint in the same location as this main program
print(os.getcwd())

#to change by current workig dir
os.chdir("D://")
print(os.getcwd())


print(os.listdir("D://SAMRAT FILE/"))

# Creating folders
#os.mkdir("This") # creates a folder
#os.makedirs("This/ That") # creates a subdir into a non existing dir
print(os.getcwd())


# to rename sth
os.chdir("D://SAMRAT FILE/Documents/Programing/Programming/Python Programs/Practice/")

print(os.getcwd())
print(os.listdir("D://SAMRAT FILE/Documents/Programing/Programming/Python Programs/Practice/"))
#os.rename("sowpods.txt", "wordlist.txt")
print(os.listdir("D://SAMRAT FILE/Documents/Programing/Programming/Python Programs/Practice/"))

#to get environment variable
print(os.environ.get("Path"))

# to join paths especially while using "/"
# print(os.path.join("D://", "/wordlist.txt"))


# to check if a certain file/folder exists or not
print(os.path.exists("D://Haha")) # > it doesnt exist so gives false
print(os.path.exists("D://SAMRAT FILE")) # > it exists so gives true

# to specify a folder or file
print(os.path.isfile("D://SAMRAT FILE")) # > it isnt a file so gives false