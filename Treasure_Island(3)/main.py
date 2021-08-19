print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
choice1= input("You are at cross road.Where do you want to go 'Left' or 'Right'?\n")
choice1_in_lowercase=choice1.lower()
if choice1_in_lowercase=="left":
  choice2=input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat and 'swim' to swim across.\n")
  choice2_in_lowercase=choice2.lower()
  if choice2_in_lowercase=="wait":
    choice3=input("You arrived at unharmed place of island and near to treasure , so choose any one colour of door from 'red','yellow','blue'.\n")
    choice3_in_lowercase=choice3.lower()
    if choice3_in_lowercase=="blue":
      print("You are member of Blue family Now and found Treasure...You win the game")
    elif choice3_in_lowercase=="red":
      print("Burned by Fire.Game Over.")
    elif choice3_in_lowercase=="yellow":
      print("Eaten by beasts.Game Over.choice3")
    else:
      print("Game Over.")


  else:
    print("Ohhh....you was near to crocodile Game Over.")
else:
  print("Oops!! You fall....Game Over.")
