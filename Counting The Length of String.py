def string_length(string):
    count = 0
    for a in string:
        count = count + 1
    return count


ask = input("Enter any word: ")
print("The no. of letters in " + ask + " is " + str(string_length(ask)))

print(
    input("""
    This program is exiting.
    Press any key and hit Enter.........
    
    """))


