__author__ = 'BenDiegel'

#open programs
#save text
#play game
#dice roller (up to 3 dice at a time!)

import random
import pickle
import subprocess


#lists for saving text data
global saveList
global saveEntry
saveList = ['save 1.txt', 'save 2.txt', 'save 3.txt']
saveEntry = ["", "", ""]

#text reader data that reads 3 seperate text files that were made from the text editor
def textReader():
    userChoice = input("What save would you like to open: 1, 2, or 3?\n")
    if userChoice == "1":
        file = open(saveList[0], 'rb')
        text = pickle.load(file)
        print(text)
        input("Press ENTER to leave\n")
        mainProgram()
    elif userChoice == "2":
        file = open(saveList[1], 'rb')
        text = pickle.load(file)
        print(text)
        input("Press ENTER to leave\n")
        mainProgram()
    elif userChoice == "3":
        file = open(saveList[2], 'rb')
        text = pickle.load(file)
        print(text)
        input("Press ENTER to leave\n")
        mainProgram()

#text editor that can save 3 seperate text files
def textEditor():
    print("What would you like to write?")
    userEntry = input()
    if input("Would you like to save?\n") == "yes":
        saveChoice = input("Save 1, 2, or 3?\n")
        if saveChoice == "1":
            saveEntry[0] = userEntry
            file = open(saveList[0], 'wb')
            pickle.dump(saveEntry[0], file)
            file.close()
        elif saveChoice == "2":
            saveEntry[1] = userEntry
            file = open(saveList[1], 'wb')
            pickle.dump(saveEntry[1], file)
            file.close()
        elif saveChoice == "3":
            saveEntry[2] = userEntry
            file = open(saveList[2], 'wb')
            pickle.dump(saveEntry[2], file)
            file.close()
    else:
        input("Deleting text...\n")
        mainProgram()
    mainProgram()

#rolls 1-4 dice and then outputs the answer
def diceRoller():
    diceAmount = input("How many dice would you like to roll (limit 4)?\n")
    if diceAmount == "1":
        diceFinal = random.randint(1,6)
        print("You rolled " + str(diceAmount) + " die and got " + str(diceFinal))
        userChoice = input("Would you like to roll again?\n")
        if userChoice == "yes":
            diceRoller()
        else:
            mainProgram()
    elif diceAmount == "2":
        diceFinal = random.randint(2,12)
        print("You rolled " + str(diceAmount) + " dice and got " + str(diceFinal))
        userChoice = input("Would you like to roll again?\n")
        if userChoice == "yes":
            diceRoller()
        else:
            mainProgram()
    elif diceAmount == "3":
        diceFinal = random.randint(3,18)
        print("You rolled " + str(diceAmount) + " dice and got " + str(diceFinal))
        userChoice = input("Would you like to roll again?\n")
        if userChoice == "yes":
            diceRoller()
        else:
            mainProgram()
    elif diceAmount == "4":
        diceFinal = random.randint(4,24)
        print("You rolled " + str(diceAmount) + " dice and got " + str(diceFinal))
        userChoice = input("Would you like to roll again?\n")
        if userChoice == "yes":
            diceRoller()
        else:
            mainProgram()

#this is the main menu that lists all of the avalible programs
def mainProgram():
    userChoice = input("What would you like to run?\n"
                           "1. Text Editor\n"
                           "2. Text Reader\n"
                           "3. Dice\n"
                           "4. Exit\n")
    if userChoice == "1":
        textEditor()
    elif userChoice == "2":
        textReader()
    elif userChoice == "3":
        diceRoller()
    elif userChoice == "4":
        exit()
    else:
        print("You did not make a known selection.")
        mainProgram()

mainProgram()