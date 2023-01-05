from turtle import *
import random

t = Turtle()

sides = 3
while sides<11:
    colors = random.choice(['black' , 'red' , 'green' , 'yellow', 'blue' , 'cyan' , 'SlateBlue4' , 'magenta', 'orange red', 'pink4'])
    for i in range(sides):
        t.pencolor(colors)
        t.right(360/sides)
        t.forward(100)
    sides+=1
s = Screen()
s.exitonclick()