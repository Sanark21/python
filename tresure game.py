print('''***********************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("welcome to the island")
print("you need to find the tresure")
choice1 = input('you are at a crossroad, where do you want to go? type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('you are came to lake.there is an island in the middle of lake.type "wait" to wait for boat or "swim" to across.\n').lower()
    if choice2 == "wait":
        choice3 = input("you are arrive th island . there is a house with three door.red, yellow, blue.which colour do you choose?\n").lower()
        if choice3 == "red":
            print("you got fired. game over")
        elif choice3 == "yellow":
            print("you got attacked by lion")
        elif choice3 == "blue":
            print("you got tresure")
        else:
            print("this door doesn't exist")      
    else :
        print("you got attack by tiger. game over")
else :
    print("you fell into a hole.game over.")