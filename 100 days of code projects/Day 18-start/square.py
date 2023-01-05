# from turtle import *
from turtle import Turtle, Screen

t = Turtle()
t.shape("triangle")
t.color("aqua")

for i in range(4):
    t.right(90)
    t.forward(100)


screen = Screen()
screen.exitonclick()