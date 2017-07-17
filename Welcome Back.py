__author__ = 'BenDiegel'

import random
import pickle
import shelve





def save_game():
    file = open("main.txt", 'wb')
    pickle.dump(player_name, file)
    pickle.dump(player_class, file)
    file.close()

def open_save():
    global player_name
    global player_class
    file = open("main.txt", 'rb')
    player_name = pickle.load(file)
    player_class = pickle.load(file)

def class_choose():
    global player_class
    global Str, Spd, Lck

    print("Please choose your class carefully.")
    print("1. Rouge | Str 2 | Spd 4 | Lck 6")
    print("2. Warrior | Str 5 | Spd 4 | Lck 3")
    print("3. Mage | Str 8 | Spd 1 |Lck 3")
    player_class = raw_input()

    if player_class == "rouge" or player_class == "Rouge":
        Str = 2
        Spd = 4
        Lck = 6
    elif player_class == "warrior" or player_class == "Warrior":
        Str = 5
        Spd = 4
        Lck = 3
    elif player_class == "mage" or player_class == "Mage":
        Str = 8
        Spd = 1
        Lck = 3
    else:
        print("You did not choose a class.")
        class_choose()

    print("You chose " + player_class.lower() + " is that right? (Y/N)" )
    if raw_input() == "Y":
        print("You chose " + player_class.lower())
        print("---Saving Game---")
        raw_input("\n")
        save_game()
    else:
        class_choose()

#asks name and gives world desciption. only plays when game starts first time
def game_start():
    global player_name
    print("\nWelcome to the world of Syron, I hope your travels have been well.\n")
    player_name = raw_input("May we ask your name, hero?\n")
    print("\n%s, you've been asked to come here by the council of magic. Our world\n"
          "is falling apart and we need your help to defeat the great monsters\n"
          "that are at fault. With the passing days, you will gain magical items\n"
          "that will aid you in your journey.\n") % player_name
    raw_input("--Press Enter--\n")
    print("The weapons will mostly increase your strength. Strength will increase\n"
          "the damage you do to enemies. Make sure to put on any helmet you find\n"
          "on. Those will increase your speed that helps with how many strikes you\n"
          "do, as well as your ability to dodge attacks! Lastly you have your rings,\n"
          "these can have any stat increase! Increasing your luck will allow you\n"
          "to find more and more items.\n\n"
          "Now go out there %s! Help save Syron!\n") % player_name
    raw_input("--Press Enter--\n")
    class_choose()


def game_open():
    print("Is this your first time playing? Y/N")
    if raw_input() == "N":
        open_save()
    else:
        game_start()

game_open()



