

def biggest_guy(num1, num2, num3):
    if num2 < num1 > num3:
        return num1
    elif  num3 < num2 > num1:
        return num2
    else:
        return num3



print(biggest_guy(3,2,1))


# We can use "max" too :

#  def sad(n1 , n2 , n3):
#    return max(n1 , n2 , n3)
#   print(sad(9 , 6 , 3))
