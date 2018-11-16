from turtle import *
from random import randint
colorlist = ["AliceBlue", "AntiqueWhite", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "BlueViolet", "brown", "burlywood", "CadetBlue", "chartreuse", "chocolate", "coral", "CornflowerBlue", "cornsilk", "cyan", "DarkBlue", "DarkCyan", "DarkGoldenrod", "DarkGray", "DarkGreen", "DarkGrey", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGrey", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue", "firebrick", "FloralWhite", "ForestGreen", "gainsboro", "GhostWhite", "gold", "goldenrod", "green", "GreenYellow"]
import shapes_function

## ======== Exercise 2 ==============
## create shapes. Function -> please refer to shapes_function 
## 4 arguments.
## sides : how many sides for the shape?
## mvRight: 180 degree - shape's internal angle
## shape Color: just for fun
## fwd: default 100 for all shapes besides circle
## -----
shapes_function.shapes(3, 120, "DarkOliveGreen1")  # Equilateral Triangle
shapes_function.shapes(4, 90, "chartreuse") # Square
shapes_function.shapes(5, 72, "DarkOrange") # Pentagon
shapes_function.shapes(6, 60, "firebrick") # Hexagon
shapes_function.shapes(8, 45, "PaleVioletRed") # Octagon
shapes_function.shapes(5, 144, "gold") # Star
shapes_function.shapes(40, 9, "coral", 10) # circle

## ======== Exercise 3 ==============
##  function -> please refer to shapes_function
## arg1/ fwd : 
## arg2 /fill: if True: fill / else: outline
shapes_function.shapes_fill(6, 60, "firebrick", 200, True) # Hexagon

# ## ======== Exercise 4 ==============
# ## --- Star on Night Sky
shapes_function.nightSky(25, 10)

## ======== Artistic Project2-1 ==============
## Function --> please refer to shapes_function
## arg2/ howMany: No of times to display the object 
shapes_function.art1(10)  # Call Function

## ======== Artistic Project2-2 ==============
## CIRCLE COMING TO YOU
## colorlist list is on first part of this file.
## ----
for i in range(len(colorlist)):
    pencolor(colorlist[i])
    speed(50)
    width(i*7)
    forward(i)
    right(15)
