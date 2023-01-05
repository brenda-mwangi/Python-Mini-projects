from turtle import *
import random

t = Turtle()
s = Screen()

t.speed(0)
t.width(5)

s.colormode(255)

def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb
def spirograph(size_of_gap):

    for i in range(int(360 / size_of_gap)):
        t.color(randomcolor())
        t.circle(100)
        t.right(size_of_gap)

spirograph(10)
s.exitonclick()    