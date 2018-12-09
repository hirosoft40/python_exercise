## ==============================
## 1. Hello, you!
def helloYou(name):
    name = input("What is your name? ")
    print ('Hello, {}!'.format (name))

## ======= ERROR HANDLING========
## 2. Hello, you!
def helloYouLen(name):
    name = input("What is your name? ".upper()).upper()
    print ('HELLO, {}! YOUR NAME HAS {} LETTERS IN IT! AWESOME!'.format (name, len(name)))
## ==============================
## 3. Madlib
def madLib():
    print ("Please fill in the blanks below:")
    name = input("What is your name? ")
    cuisine = input("What is your favorite cuisine?")
    print ('%s\'s favorite cuisine is %s! Yummy in my tummy!' %(name, cuisine))
#=======list version=====
## 4.dayofthe week
def dayOfTheWeek():
    day = int(input('Day (0-6)? '))
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if day in range(len(week)):
        print (week[day])
    else:
        print ("Type in number between 0 to 6!")
## ==============================
## 5. Work or Sleep In?
def workOrSleepIn():
    day = int(input("Day (0-6)?"))
    if day < 0 or day > 6:
        print ("Type in number between 0 to 6.")
    elif day > 0 and day < 6:
        print ("Go to work!!")
    else:
        print ("Sleep in.")
## ==============================
## 6. Celsius to Fahrenheit
def temperature():
    cel = int(input('Temperature in Celsius?'))
    fah = round(cel * 1.8 + 32, 2)   # calculating Fahrenheit. Rounded to 2 decimals for display purpose.
    print ("%d celsius is %.2f Fahrenheit." % (cel, fah))

## ==============================
## 7. tip calculator
def tipCalculator():
    bill = int(input("What is the total bill amount?"))
    srv = input("Level of service? Good / Fair / Bad ").lower()
    tip = 0
    total = 0

    tip_base = {
        'good': 0.2,
        'fair': 0.15,
        'bad' : 0.1
    }

    if bill < 0:
        print ("Type in amount larger than 0.")
    elif srv not in tip_base.keys():
        print ('ERROR: Type in Good or Fair or Bad.')
    else:
        tip = bill * tip_base[srv]
        total = bill + tip
        print ('Tip amount ${:.2f} Total amount ${:.2f}'.format(tip, total))

## ==============================
# 8. tip calculator2
def tipCalculator2():
    bill = int(input("What is the total bill amount?"))
    srv = input("Level of service? Good / Fair / Bad ").lower()
    ppl = int(input("How many ways would you like to split the bill?"))
    tip = 0
    total = 0

    tip_base = {
        'good': 0.2,
        'fair': 0.15,
        'bad' : 0.1
    }

    if bill < 0:
        print ("Type in amount larger than 0.")
    elif srv not in tip_base.keys():
        print ('ERROR: Type in Good or Fair or Bad.')
    else:
        tip = bill * tip_base[srv]
        total = bill + tip
        ppl = total / ppl
        print ('Tip amount ${:.2f} Total amount ${:.2f}'.format(tip, total))
        print ('Amount per person: ${:.2f}'.format(ppl))
## ==============================
## 9. 1 to 10
def print1to10():
    i = 0
    while i < 10:
        i += 1
        print (i)
## ==============================
## 10. coins
def coins():
    ans = 'yes'
    coin = 0
    while ans == "yes":
        ans = input("You have %d coins. Do you want another? " % (coin)).lower()
        coin += 1
        if ans == "no":
            print ("Bye!")
            break
## ==============================
# 2018/11/14 Guess a number game
import random 

# === guess the number 
# continue or not
def again():
    again = input("Do you want to play again? (Y or N)").lower()
    if again == 'y':
        guess()
    else:
        print ("Good bye. See you soon.")

def guess():
    num = random.randint(1,10) # generate random number
    count = 5       # Maximum that you can try

    # initial intract with user.
    print ("I am thinking of a number between 1 and 10. You have %d gueeses left." % count)
    user_num = int(input("What's the number? : "))

    # user can try 5 times.
    while count > 0:

        # error handling for non-expected numbers.
        if user_num > 10 or user_num < 0:
            print ("Type in number between 1 and 10. ")
        
        # User won => break out of loop
        elif user_num == num:
            print ("Yes, %d is the number! You won!" % user_num)
            again()
            break
        
        # number off by 2 or more => too high/too low
        elif user_num > num + 1: 
            print("Nope, %d is too high." % user_num)
        elif user_num < num - 1:
            print ("Nope, %d is too low." % user_num)
        
        # number off by 1 => close
        else:
            print ("Nope, %d is close." % user_num)

        count -= 1
        # check remaining number of guesses.
        if count > 0: 
            user_num = int(input("You have %d guesses left. What's the number? : " % count))    
        else:          
            print("You run out of the guesses!")
            again()
        
## ==============================
## 1. 1 to 10
## ----


def print1to10():
    for i in range(1, 11):
        print(i)

# ## ==============================
# ## 2. n to m
# ## ----


def ntom():
    start = int(input("Start from: "))
    end = int(input("End on: "))

    if start > end:  # error handling for start larger than end
        print("Start must be lower number than end %d" % (end))
        start = int(input("Start from: "))
    else:
        for i in range(start, end+1):
            print(i)

# ## ==============================
# ## 3. Print odd numbes
# ## ----


def printOddNum():
    for i in range(1, 11):
        if i % 2 > 0:
            print(i)

# ## ==============================
# ## 4. Print a Square : Print a 5x5 square of * characters. Example output:
# ## ----


def printSquare(size):
    for i in range(size):
        print("printing a square---- ")
        print('*' * size)

# ## ==============================
# ## 5. Print a Square II : Print a NxN square of * characters. Prompt the user for N.
# ## ----


def printSquareNtimes():
    num = int(input("How many times?:"))
    for i in range(num):
        star = ""
        for j in range(num):
            star += "*"
        print("printing a square---- ")
        print(star)

# ## ==============================
# ## 6. Print a Box : Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:
# ## ----


def printBox():
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
        print(star)

## 7. Print a Triangle ==========NOT DONNNNNN


def printATriangle():
    print("3 rows triangle---- ")
    print("  *  \n *** \n*****")

# ## 8. Print a Triangle II


def printATriangleNheight():
    height = int(input("Height?"))
    print("printing a triangle with your input height.")
    i = 1
    x = height-2
    while i < height:
        print(" " * x, "*" * ((i-1)*2+1))
        i += 1
        x -= 1

# # answer learned from Ray
# height = 4
# for i in range(height):
#     print ("*" + ("*" *2*i))
# # answer
# xr = 10
# for x in range (0,xr);
#     spaces = xr -x - 1
#     stars = x * 2 + 1
#     print (' ' * spaces + '*' * stars)

## ==============================
## 9. Multiplication Table 1 to 10
## ----


def multiplicationTable():
    print("multiplication table")
    for i in range(1, 11):       # outer numbers
        for j in range(1, 11):   # inner numbers
            print(i, " X ", j, " = ", i*j)

## ==============================
## Bonus: Print a Banner : Text? Welcome to DigitalCrafts
## ----


def printBanner():
    msg = input("Text? : ")
    star = ""
    for i in range(len(msg)+4):
        star += "*"

    print(star)  # since only 3 rows, I just printed them instead of loop
    print("*", msg, "*")
    print(star)

## ==============================
## Bonus: Triangle Numbers
## Print the first 100 triangle numbers. What is a triangle number? Read this: https://www.mathsisfun.com/algebra/triangular-numbers.html.
## ----


def triangleNumber():
    sum = 0
    for i in range(1, 101):
        sum += i   # triangle num is sum of all numbers
        print(i, " : ", sum)

## ==============================
## Bonus: Factor a Number
## Given a number, print its factors. What are factors? https://www.khanacademy.org/math/pre-algebra/factors-multiples/divisibility-and-factors/v/finding-factors-of-a-number
## ----


def fuctorNumber():
    num = int(input("Find out factors. Type number larger than 0: "))

    while num < 1:  # error handling for 0 or smaller numbers
        num = int(input("Find out factors. Type number larger than 0: "))

    for i in range(1, num+1):  # print factors
        if num % i == 0:
            print(i)


## ==============================
## 1 sum the numbers
def sumList():
    lis = [1,16,18,19, 2050, 9.84, -10, 0]
    sum = 0
    for i in lis:
        sum += i
    print (sum)

## ==============================
## 2 Larger Number
def maxList():
    lis = [1,16,18,19, 2050, 9.84, -10, 0]
    print (max(lis))

## ==============================
## 3 smallest Number
def minList():
    lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
    print (min(lis))

## ==============================
## 4 even number
def even():
    lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
    for i in lis:
        if i%2 == 0:
            print ("even number is :", i)

## ==============================
## 5 positive number
def positive():
    lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
    for i in lis:
        if i > 0:  # 0 is not negative nor positive
            print ("positive number is :", i)

## ==============================
def newListPositiveNo():
    lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
    newlis =[]
    ## 6 new list of positive number
    for i in lis:
        if i > 0:  # 0 is not negative nor positive
            newlis.append(i)
    print (newlis) # result not sorted

## ==============================
## 7 Multiply a list
def multiplyNum():
    lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
    num = int(input("Type in a number: ")) # factor number
    multiplyNum = []
    for i in lis:
        multiplyNum.append(i * num)
    print (multiplyNum)

## ==============================
##8 Multiply Vectors
def multiplyVector():
    list1 = [1,2,3]
    list2 = [4,5,6]
    pairList = []
    for i in range(len(list1)): # as 2 lists are same length, loop by index
        pairList.append(list1[i] * list2[i])
    print (pairList)

## ==============================
##9 & 10 Matrix Addition
##======= #10 worked on my solution for #9======
def matrixAddition():
    matList1 = [[1,2],[3,4]]
    matList2 = [[5,6],[7,8]]
    newMatList = []

    for i in range(len(matList1)):
        for l in range(len(matList1[i])):
            newMatList.append(matList1[i][l] + matList2[i][l])
    print (newMatList)

## ==============================
##11 De-dup : new list without duplicates
## ----
def deDup():
    alist = [1,2,3,"ab","cd",3,"ab","one", "two", "one"]
    newList = [alist[0]]
    # loop all the element in a list
    for ele in alist:
        if ele not in newList: newList.append(ele)
    print (newList)


## ==============================
## 1 Change to uppercase
def changeToUpperCase():
	somestr = input("Type in to change to Uppercase.")
	print (somestr.upper())

## ==============================
## 2 Capitalizing 
def changeToCapitalizing():
	somestr = input("Type in to change to Capitalize.")
	print (somestr[0].upper() +somestr[1:] ) 

## ==============================
## 3 Reverse letters 
def reverseLetters():
	somestr = input("Type in to reverse letters.")
	print (somestr[::-1]) 

## ==============================
## 4 Leetspeak
def leetspeak():
	leet = {
		"A": "4",
		"E": "3",
		"G": "6",
		"I": "1",
		"O": "0",
		"S": "5",
		"T": "7"
	}
	msg = ""
	somestr = input("Type in to leet.")
	for i in somestr.upper():
		if i in leet.keys():
			msg += leet[i].lower()  # per sample, changed to lowercase.
		else:
			msg += i.lower() # per sample, changed to lowercase.
	print (msg)

## 5 long-long vowels
## test case: good, nachocheese, spoon, food, eat, soup, 
## ????? NOT FINISHED for nahcocheese. and I feel these are nested too much.

def longlongVowles():
	longV = input("What is your favorite long vowel word?: ")
	vow = ('a','e','i','o','u') # vowels tuple 
	veryLongV = ""     # string to hold loooong vowel
	vowCount = 0       # count how many vowels in word input by user
	print("Make long vowle to looong vowel ===> ")
	for i in longV: 
		veryLongV += i
		if i in vow:
			tempVow = i
			vowCount += 1
			while vowCount < 4:
				veryLongV += i
				vowCount += 1

	print (veryLongV)

## ==============================
## 6 Caesar Cipher
## ----
def caesarCipher():
	plain = input("Plain message: ")
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	#plain = "defend the east wall of the castle" # TEST CASE
	newMsg = ""

	for i in plain:
		if i == " ":
			newMsg += " "
		else: # not enough time for number error handling
			# find the letter in alphabet
			newMsg += alphabet[alphabet.index(i)+1] 
	print("Created cipher  ===> ")
	print (newMsg)