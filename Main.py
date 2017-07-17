# This is a text base rpg adventure game created by Ben Diegel.
# These first lines are variables and such used throughout the game.
# Go to "Adventure Start" line to see the game


damage = 1
chooseClass = "Noob"

# This is my advance line and stats function
def statEnter():
    line = raw_input("\n---Press 'Enter' to advance, or type 'stats' to see your current stats.---\n")
    if line == "stats":
        print "\n-------------"
        print "Damage = " + str(damage)
        print "Class = " + str(chooseClass)
        print "-------------"
        print "\n"
    else:
        str()

# This is the easy enter option
def easyEnter():
    raw_input("\n---Press enter to advance---")

# ----------------------------------------------------------------------------------------------------------------------
# Character creation

print "\n\nWelcome to the Adventure your damage begins at 1.\n" \
      "later you will be able to pick a class to play!"

statEnter()

name = raw_input("What is your name?\n")

print "\nWelcome %s to the world of Ayocyte!\n" \
      "This world is full of adventure, monsters, and rewards!\n" \
      "So sit tight and enjoy the ride!" % name

easyEnter()

chooseClass = raw_input("\nPlease choose your class (Pirate, or Ninja)\n")

if chooseClass == "Ninja":
    print "\nYour damage has increased by 1"
    damage = 2
    print "Damage = " + str(damage)
elif chooseClass == "Pirate":
    print "\nYour damage has increased by 2!"
    damage = 3
    print "Damage = " + str(damage)

else:
    print "Please choose Pirate or Ninja!"
    chooseClass = raw_input()
    if chooseClass == "Ninja":
        print "\nYour damage has increased by 1"
        print "damage = 2"
    elif chooseClass == "Pirate":
        print "\nYour damage has increased by 2"
        print "damage = 3"
    else:
        print "\nYou did not choose a class and went home"

statEnter()

# ----------------------------------------------------------------------------------------------------------------------
# Adventure starts

print "Welcome young %s! My name is Nephoid, I will be your guide for this \njourney." \
      "\nCome walk with me and I will tell you more about this world" % chooseClass
easyEnter()
yn = raw_input("\nDo you go with Nephoid (Yes or No)\n")
if yn == "Yes":
    print "\nOkay! Lets go!"
else:
    print "\nWell if you think you can make it yourself"
    easyEnter()
    print "\nYou were instantly killed by a giant bear"
    easyEnter()
    raise SystemExit

print "\nSo this is an enemy"

raw_input()


