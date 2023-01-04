# from turtle import Turtle, Screen

# my_screen = Screen()

# print(my_screen.canvheight) #has an attribute canvheight

# timmy = Turtle()
# timmy.shape("turtle")  #can do this
# timmy.color("blue")    #can do this
# timmy.forward(100)  #can do this


# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', ' Water', 'Fire'])

table.align = 'l'
# set_style = align('l')
print(table)
