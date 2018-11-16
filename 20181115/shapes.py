from turtle import *
from random import randint

# ## = Need this function For Exercise 4 and Art Project ==============
def changeLocation():
    # change locations
    penup()
    x, y = randint(-200, 200), randint(-200, 200)
    goto(x, y)
    pendown()

## ======== Exercise 2 ==============
## create shapes. 4 arguments.
## sides : how many sides for the shape?
## mvRight: 180 degree - shape's internal angle
## shape Color: just for fun
## fwd: default 100 for all shapes besides circle
## -----
def shapes(sides, mvRight, shapeColor, fwd=100):
    pensize(15) # optional
    color(shapeColor) #optional
    for i in range(sides):
        forward(fwd)
        right(mvRight)

shapes(3, 120, "DarkOliveGreen1")  # Equilateral Triangle
shapes(4, 90, "chartreuse") # Square
shapes(5, 72, "DarkOrange") # Pentagon
shapes(6, 60, "firebrick") # Hexagon
shapes(8, 45, "PaleVioletRed") # Octagon
shapes(5, 144, "gold") # Star
shapes(40, 9, "coral", 10) # circle

## ======== Exercise 3 ==============
## fwd : 
## fill: if True: fill / else: outline
def shapes(sides, mvRight, shapeColor, fwd,fill):
    pensize(15) # optional
    if fill == True:
        fillcolor(shapeColor)
    else: 
        color(shapeColor) #optional
    
    for i in range(sides):
        forward(fwd)
        right(mvRight)

shapes(6, 60, "firebrick", 200, True) # Hexagon

# ## ======== Exercise 4 ==============
# ## --- Star on Night Sky

def nightSky(noOfStar, fwd):
    bgcolor("Navy")
    color("gold")
    pensize(5) # optional
    while noOfStar > 0:
        speed(10)
        fillcolor("gold")
        begin_fill()
        changeLocation()  
        # make stars
        for i in range(5):
            forward(fwd)
            right(120)
            forward(fwd)
            right(72-120) # (-72: 360/5)
        noOfStar -= 1
        end_fill()

nightSky(25, 10)

## ======== Artistic Project2-1 ==============
## arg1/ color: pencolor
## arg2/ howMany: No of times to display the object 
def art1(color, howMany):
    pencolor(color)
    while howMany > 0:
        for i in range(40):
            speed(15)
            forward(150)
            right(170)
        changeLocation()
        stamp()
        howMany -= 1

art1("Orange", 10)  # Call Function

## ======== Artistic Project2-2 ==============
## CIRCLE COMING TO YOU
## ----
colorlist = ["AliceBlue", "AntiqueWhite", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "BlueViolet", "brown", "burlywood", "CadetBlue", "chartreuse", "chocolate", "coral", "CornflowerBlue", "cornsilk", "cyan", "DarkBlue", "DarkCyan", "DarkGoldenrod", "DarkGray", "DarkGreen", "DarkGrey", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGrey", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue", "firebrick", "FloralWhite", "ForestGreen", "gainsboro", "GhostWhite", "gold", "goldenrod", "green", "GreenYellow"]
for i in range(len(colorlist)):
    pencolor(colorlist[i])
    speed(50)
    width(i*7)
    forward(i)
    right(15)



## ===== Artistic Project 1 to be tried soon ====