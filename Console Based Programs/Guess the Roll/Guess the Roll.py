print("""
                                ---------- Guess the Roll XD ----------
""")

from random import randint
from time import sleep
def get_user_guess():
  guess = int(input("Enter your guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides*2
  print(
      """

      """
  )
  print("                                             Rule:")
  print  ("                                  The maximum possible value is %s" % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print ("Its invalid!!")
  else :
    print("Rolling...")
    sleep(2)
    print(
      """
      """
  )
    print("The first roll is %s" %(first_roll))
    sleep(1)
    print("The second roll is %s" %(second_roll))
    sleep(1)  
    print(
      """
      """
  )
    total_roll = first_roll + second_roll
    print ("Result...")
    sleep(1)
    if guess == total_roll:
      print("                                           YOU WON!!!")
    else:
      print("                                           YOU LOSE!!!")
roll_dice(6)


print (
      """
      """
  )

print(
    input("""
                                         This program is exiting.
                                    Press any key and hit Enter.........
    
    """))
    
    

  
  
  
  
  

