import colorgram as cl

colors = cl.extract('colorspic.jpg', 30)

colors_list = []

for col in colors:
    colors_list.append((col.rgb.r, col.rgb.g, col.rgb.b))

#for col in colors_list:
#    print(col)
