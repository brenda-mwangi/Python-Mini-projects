from turtle import Turtle, Screen
import random
rgb_colors = [(202, 164, 109), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

t = Turtle()
s = Screen()

s.colormode(255)

t.speed(0)
t.width(10)
t.shape("circle")

def random_colour():
    return random.choice(rgb_colors)

x=-350
y = -250

while y<250:
    y+=50
    t.penup()
    t.goto(-300,y)
    t.pendown()
    for h in range(10):
        x+=50
        t.stamp()
        t.color(random_colour())
        t.penup()
        t.forward(50)
        t.pendown()
        
t.hideturtle()

s.exitonclick()