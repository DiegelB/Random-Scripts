__author__ = 'BenDiegel'

""" This is a magic 8-ball program.
 When it receives your question ot randomizes
 1-N, what ever number it generates corresponds to
 the output response."""

import random

def magic():
    answer = raw_input("\nWhat is your question?\n")
    if answer == "":
        print "You did not ask a question."
        magic()
    rand = random.randint(1, 11)
    if rand == 1:
        print "It is certain."
    elif rand == 2:
        print "Without a doubt."
    elif rand == 3:
        print "As I see it, yes."
    elif rand == 4:
        print "Yes"
    elif rand == 5:
        print "Signs point to yes."
    elif rand == 6:
        print "Ask again later."
    elif rand ==7:
        print "Better not tell you now."
    elif rand == 8:
        print "Cannot predict now."
    elif rand == 9:
        print "Don't count on it."
    elif rand == 10:
        print "Very doubtful."
    elif rand == 11:
        print "Outlook not so good."
    newQ = raw_input("Type 'exit' to stop playing.\n")
    if newQ == "exit" or newQ == "Exit":
        exit()
    else:
        magic()


print "\nWelcome to The Magic 8-Ball"
magic()