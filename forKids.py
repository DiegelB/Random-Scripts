#! /usr/bin/python3

import turtle
import random
t = turtle.Pen()
r = random.randint(0,360)
t.pensize(5)
t.speed(0)
color = ['red', 'pink', 'blue', 'purple', 'orange', 'green', 'yellow']
randColor = random.choice(color)
def coolLoop(rand, color):
	for x in range(0,100):
		t.color(random.choice(color))
		t.forward(x*2)
		t.left(rand)
		t.left(rand)
		t.backward(x)
		t.left(rand)
		t.forward(x)
	turtle.done()

coolLoop(r, color)
