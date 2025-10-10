print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
direction=input('You come to a fork in the road. Type "left" or "right"').lower()
if direction == "left":
    water=input('You walk for several miles. Eventually you come to a large, stagnant body of water. You notice a dock. Type "wait" to wait for the boat, or "swim" to swim across.').lower()
    if water=="wait":
        door=input('The boat takes you to a small island where you notice a house with 3 doors, one red, one blue, and one yellow. Which door do you try?').lower()
        if door=="yellow":print("Stepping inside the yellow door, you find a room filled with treasure and the secret to eternal happiness. Congratulations, you win!")
        if door=="red":print("Stepping inside the red door, you are immediately engulfed in flames and proceed to burn to death. Game over")
        if door=="blue":print("Stepping inside the blue door, you are immediately attacked and eaten by savage beasts. Game over")
    else:print("You remember you cannot swim and proceed to drown. Game over.")
else:print("You run into a group of road bandits who proceed to rob and kill you. Game over.")