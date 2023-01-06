from turtle import Turtle, Screen
import random
# t, tim, timmy, tom, tommy, tosh = Turtle(), Turtle(), Turtle(),Turtle(),Turtle(),Turtle()
# turtles = [t, tim, tom, timmy, tommy, tosh]

s = Screen()
s.setup(width = 500, height = 400)
is_race_on = False

user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a rainbow color")
print(user_bet)

colors = ["red", "orange","yellow","green","blue", "purple"]

y = -110
turtles = []
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    turtles.append(t)
    turtles[i].penup()
    turtles[i].goto(x = -230, y = y)
    # turtles[i].pendown()
    y+=50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                g = f"You've won!! The winning color is {winner}"
            else:
                g = f"You've lost. The winning color is {winner}"
            print(g)
        else:
            turtle.forward(random.randint(0,10))

s.exitonclick()
