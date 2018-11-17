## ==============================
## 1. 1 to 10
## ----
for i in range(1,11):
    print (i)

# ## ==============================
# ## 2. n to m
# ## ----
start = int(input("Start from: "))
end = int(input("End on: "))

if start > end:  # error handling for start larger than end
    print ("Start must be lower number than end %d" % (end))
    start = int(input("Start from: "))
else:
    for i in range(start, end+1):
        print (i)

# ## ==============================
# ## 3. Print odd numbes
# ## ----
for i in range(1,11):
    if i%2 > 0 : print (i)

# ## ==============================
# ## 4. Print a Square : Print a 5x5 square of * characters. Example output:
# ## ----
for i in range(5):
    star = ""
    for j in range(5):
        star += "*"
    print (star)

## ~~~~~ ans. Take away : no need to define string. connect with *
for i in range(size):
    print ('*' * size)

# ## ==============================
# ## 5. Print a Square II : Print a NxN square of * characters. Prompt the user for N. 
# ## ----
num = int(input("How many times?:"))
for i in range(num):
    star = ""
    for j in range(num):
        star += "*"
    print (star)

# ## ==============================
# ## 6. Print a Box : Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:
# ## ----
width = int(input("Width: "))
height = int(input("Height: "))

for row in range(height):
    star = ""   
    for col in range(width):
        # first row, last row => all stars
        # first column and last column in other row => stars
        if row == 0 or row == height-1 or col == 0 or col == width-1:
            star += "*"
        else:
            star += " "
    print (star)

## 7. Print a Triangle ==========NOT DONNNNNN
print ("  *  \n *** \n*****")

# ## 8. Print a Triangle II
height = int(input("Height?"))
i = 1
x = height-2
while i < height:
    print (" " * x, "*" * ((i-1)*2+1) )
    i+= 1
    x-=1

# # answer learned from Ray
# height = 4
# for i in range(height):
#     print ("*" + ("*" *2*i))
# # answer
xr = 10
for x in range (0,xr);
    spaces = xr -x - 1
    stars = x * 2 + 1
    print (' ' * spaces + '*' * stars)

## ==============================
## 9. Multiplication Table 1 to 10
## ----
for i in range(1,11):       # outer numbers
    for j in range(1,11):   # inner numbers
        print (i, " X ", j, " = ", i*j)

## ==============================
## Bonus: Print a Banner : Text? Welcome to DigitalCrafts
## ----
msg = input("Text? : ")
star = ""
for i in range(len(msg)+4):
    star += "*"
    
print (star) # since only 3 rows, I just printed them instead of loop
print ("*", msg, "*")
print (star)

## ==============================
## Bonus: Triangle Numbers
## Print the first 100 triangle numbers. What is a triangle number? Read this: https://www.mathsisfun.com/algebra/triangular-numbers.html.
## ----
sum = 0
for i in range(1,101):
    sum += i   # triangle num is sum of all numbers
    print (i," : ", sum) 

## ==============================
## Bonus: Factor a Number 
## Given a number, print its factors. What are factors? https://www.khanacademy.org/math/pre-algebra/factors-multiples/divisibility-and-factors/v/finding-factors-of-a-number
## ----
num = int(input("Find out factors. Type number larger than 0: "))

while num < 1: # error handling for 0 or smaller numbers
    num = int(input("Find out factors. Type number larger than 0: "))

for i in range(1,num+1): # print factors
    if num % i == 0:
        print (i)