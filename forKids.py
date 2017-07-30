#! /usr/bin/python3

import turtle
import random
t = turtle.Pen()
s = turtle.Screen()
r = random.randint(0,360)
t.pensize(5)
t.speed(0)
color = ['red', 'pink', 'blue', 'purple', 'orange', 'green', 'yellow']
randColor = random.choice(color)
s.title("My Turtles")

def startDraw(color):
	t.color(color[0])
	t.penup()
	t.goto(0,200)
	t.write("Dick")
	s.exitonclick()


def coolLoop(rand, color):
	t.ht()
	for x in range(0,150):
		t.color(random.choice(color))
		t.forward(x*2)
		t.left(rand)
		t.left(rand)
		t.backward(x)
		t.left(rand)
		t.forward(x)
	turtle.done()
startDraw(color)
coolLoop(r, color)
