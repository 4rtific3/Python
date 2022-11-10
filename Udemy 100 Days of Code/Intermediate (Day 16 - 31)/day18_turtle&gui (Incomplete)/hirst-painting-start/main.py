###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import os
import colorgram

rgb_colors = []
colors = colorgram.extract(os.path.join('C:\Users\jg2jo\OneDrive\Documents\GitHub\Python\Udemy 100 Days of Code\day18_turtle&gui\hirst-painting-start\image.jpg', 30))
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)