##This code will not work in repl.it as there is no access to the colorgram package here.###
#We talk about this in the video tutorials##
import colorgram
rgb_colors = []
colors = colorgram.extract('C:/Users/USER/Desktop/Python-Mini-projects/100 days of code projects/Day 18-start/Hirst Painting/image.jpg', 30)
    
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)