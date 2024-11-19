# Snake Water Gun Game

import random

def gameWin(comp,you):
    #if two value are equals ,declare a tie !
   if comp == you:
       return None
       # check for all posibilities when computer chose s
   elif comp == 's':
       if you == 'w':
           return False
       elif you == 'g':
           return True
           
    # check for all posibilities when computer chose w
   elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
      # check for all posibilities when computer chose g      
   elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True    

print  ("comp Turn : Snake(s) Water (w) or Gun (g)?")

randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 's'

elif randNo == 2:
    comp = 'w'

elif randNo == 3:
    comp = 'g'

you = input("your's Turn:Snake(s) Water(w) or Gun(g)")

a=gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("The game is Tie !!")

elif a:
    print("You win !!")
else :
    print("You Lose!!")   