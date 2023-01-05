from turtle import Turtle,Screen

t = Turtle()

for i in range(50):
    t.forward(10)
    t.penup()
    t.forward(5)
    t.pendown()

s = Screen()
s.exitonclick()