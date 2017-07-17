#Author MLGSkelly

#Classic text-based adventure game,
#that focuses on randomly generated
#items and new-age leveling system.


import random
import subprocess
import pickle


#This is the starting game function. Will play on
#any new game.

global save
global playerName
global playerHp
global playerExp
global playerItems

save = 'Current_Save.txt'

playerHp = 100
playerExp = 0
playerItems = []


#Entering program that shortcuts a prompt to the
#next screen.
def easyEnter():
    raw_input("---Press Enter to Procced---\n")


#Scene that opens the application. Will load files when neccesary
def openScene():
    print("Have you explored these lands before traveler?")
    userChoice = raw_input()
    if userChoice == "yes" or userChoice == "Yes":
      print("Would you like to load your current save?")
      userChoice = raw_input()
      if userChoice == "yes" or userChoice == "Yes":
          file = open(save, 'rb')
          playerName = pickle.load(file)
          playerHp = pickle.load(file)
          playerExp = pickle.load(file)
          playerItems = pickle.load(file)
          print("SAVE LOADED")
          print(str(playerHp))
          easyEnter()
      else:
          openScene()
    else:
        newGame()


#The scene that new players will see that asks their name and gives them weapons/tutorial
def newGame():
    print("Welcome traveler, my name is PLACEHOLDER. I will be guiding you\n"
          "through this wonderful world. May I ask your name?")
    userType = raw_input()
    playerName = userType
    print("Thank you %s. I see that you are not well equiped for these lands\n"
          "please take my sword and dagger.") % playerName
    print(playerName)
    print(playerName)
    print(playerName)
    easyEnter()
    saveGame()
    easyEnter()

#save game functuin that you can call to save all your variables
#It sees your current save to name the file correctly for
#later use.
def saveGame():
    file = open(save, 'wb')
    pickle.dump(str(playerName), file)
    pickle.dump(playerHp, file)
    pickle.dump(playerExp, file)
    pickle.dump(playerItems, file)
    file.close()


openScene()