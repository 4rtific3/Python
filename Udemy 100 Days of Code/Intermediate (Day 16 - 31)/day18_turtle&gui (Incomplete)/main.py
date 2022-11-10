import requests
import colorgram as cg

colors = cg.extract('colour_chart.jpg', 10)

print(colors)