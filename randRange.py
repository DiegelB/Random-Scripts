import random

def randomRange():
	print("Please enter random starting point")
	startPoint = input(">>"))
	print("Please enter random ending point")
	endPoint = input(">>"))

	print('Your random number between ', str(startPoint), ' and ', str(endPoint), ' is ', str(random.randint(startPoint,endPoint)))
	print("test", str(startPoint))
randomRange()
