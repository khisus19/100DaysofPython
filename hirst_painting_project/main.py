import colorgram

colors = colorgram.extract("./hirst_painting_project/hirst_1.webp", 6)

color_1 = tuple(colors[0].rgb)
color_2 = tuple(colors[1].rgb)
color_3 = tuple(colors[2].rgb)
color_4 = tuple(colors[3].rgb)
color_5 = tuple(colors[4].rgb)
color_6 = tuple(colors[5].rgb)

print(color_1)