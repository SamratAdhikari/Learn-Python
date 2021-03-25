# Else and Finally in Try Except

# Try ra Except jun sukai run bhayeni tyo bhitra run hune code finally ho!!!
# Else ko code run bhayo bhane Except ko run hunna and vice versa
# We can write more than one Except

try:
    f = open("Doesnt_Exist.txt")

except Exception as e:
    print(e)

else:
    print("Except is not running!")

finally:
    print("Run this code anyway!!!")

print("This is IMP program")