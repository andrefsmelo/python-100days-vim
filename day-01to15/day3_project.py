print('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888  
''')
print("Welcome to Treasure Island.")
print("You mission is to find a treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                   'There is an island in the middle of the lake. '
                   'Type "wait" to wait for the boat. '
                   'Type "swim" to swim across.\n').lower()
    
    if choice2 == "wait":
        choice3 = input('You arrived at the island unharmed. '
                        'There is a houde with 3 doors. One red, '
                        'one yellow and one blue. '
                        'Which colour do you chose?\n').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")     
    else:
        print("You got attacked by an angry trout. Game Over")
else:
    print("You fell in to a hole. Game Over.")
