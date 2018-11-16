## ======================
## 1. Hello
## ----
def hello(name):
    print ("Hello ", name)

## ======================
## 2. y = x + 1
## ----
import matplotlib.pyplot as plot

def f(x):
    return x+1

xs = list(range(-3, 4))
ys = []

for i in xs:
    ys.append(f(i))

plot.plot(xs, ys)
plot.show()

## ======================
## 3. square of x
## ----
import matplotlib.pyplot as plot

def f(x):
    return x**2

xs = list(range(-100, 100))
ys = []

for i in xs:
    ys.append(f(i))

plot.plot(xs, ys)
plot.show()

## ======================
## 4. Odd or Even
## ----
import matplotlib.pyplot as plot

def f(x):
    if x%2 == 0:
        return -1
    else:
        return 1

xs = list(range(-5, 5))
ys = []

for i in xs:
    ys.append(f(i))

plot.bar(xs, ys)
plot.show()

## ======================
## 5. Sine
## ----
import matplotlib.pyplot as plot
from math import sin

def f(x):
    return sin(x)

xs = list(range(-5, 5))
ys = []

for i in xs:
    ys.append(f(i))

plot.plot(xs, ys)
plot.show()

# # ======================
# # 6. Sine2
# # ----
import matplotlib.pyplot as plot
from math import sin
from numpy import arange

def f(x):
    return sin(x)

xs = arange(-5, 6,0.1)
ys = []

for i in xs:
    ys.append(f(i))

plot.plot(xs, ys)
plot.show()

## ======================
## 7. Degree conversion
## ----
import matplotlib.pyplot as plot

def convertTemp(cel):
    return round(cel * 1.8 + 32, 2)

# Added 1 more list to show the date
xs = [8, 11, 14, 12, 10, 13, 13, 11, 10, 11, 8] #temp in Houston from 11/1 to 11/11
ys = []
zs = list(range(1,12)) # November 1 to 11

for i in xs:
    ys.append(convertTemp(i))

print (ys)
plot.plot(zs, ys, xs)
plot.show()

## ======================
## 8. Play again?
## ----

def playAgain():
    res = input("Play again? Y or N: ").lower()
    if res == 'y':
        return True
    else:
        return False

## ======================
## 9. Play again?
## ----

## check response from user
def response(): 
    res2 = input("Play again? Y or N: ").lower()
    while res2 != 'y' and res2 !='n':
        print ("Invalid Input. ")
        res2 = input("Play again? Y or N: ").lower()
    return res2

## receive y/n response from response() and return True or False
def playAgain2():
    if response() == 'y':
        return True
    else:
        return False

playAgain2()
