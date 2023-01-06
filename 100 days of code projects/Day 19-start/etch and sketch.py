from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_forward():#w
    t.forward(10)
def move_back():#s
    t.back(10)
def move_right(): #a
    t.right(20)
def move_left():#d
    t.left(20)  
def clear_all(): #c
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(key = "w", fun = move_forward)
s.onkey(key = "s", fun = move_back)
s.onkey(key = "a", fun = move_right)
s.onkey(key = "d", fun = move_left)
s.onkey(key = "c", fun = clear_all)

s.exitonclick()