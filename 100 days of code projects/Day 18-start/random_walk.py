# SPEED UP
# THICKNESS
from turtle import *
import random

t = Turtle()
s = Screen()

t.speed(6)
t.width(5)

s.colormode(255)

def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb
    
for i in range(200):
    move = random.choice([90, 270, 0, 180])
    t.color(randomcolor())
    t.setheading(move)
    t.back(30)

s.exitonclick()
