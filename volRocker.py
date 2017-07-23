#! /usr/bin/python3

import os

def volume():
	print ("What would you like to set the volume at?")
	userInput = input(">>")
	userInput = userInput + "%"
	mas = """ 'Master' """
	os.system("amixer sset" + mas + userInput)

volume()


