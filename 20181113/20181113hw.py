## ==============================
## 1. Hello, you!
name = input("What is your name? ")
print ('Hello, {}!'.format (name))
## ======= ERROR HANDLING========
## 2. Hello, you!
name = input("What is your name? ".upper()).upper()
print ('HELLO, {}! YOUR NAME HAS {} LETTERS IN IT! AWESOME!'.format (name, len(name)))
## ==============================
## 3. Madlib
print ("Please fill in the blanks below:")
name = input("What is your name? ")
cuisine = input("What is your favorite cuisine?")
print ('%s\'s favorite cuisine is %s! Yummy in my tummy!' %(name, cuisine))
## ==============================
## 5. Work or Sleep In?
day = int(input("Day (0-6)?"))
if day < 0 or day > 6:
    print ("Type in number between 0 to 6.")
elif day > 0 and day < 6:
    print ("Go to work!!")
else:
    print ("Sleep in.")
## ==============================
## 6. Celsius to Fahrenheit
cel = int(input('Temperature in Celsius?'))
fah = round(cel * 1.8 + 32, 2)   # calculating Fahrenheit. Rounded to 2 decimals for display purpose.
print ("%d celsius is %.2f Fahrenheit." % (cel, fah))

## ==============================
## 7. tip calculator
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
i = 0
while i < 10:
    i += 1
    print (i)
## ==============================
## 10. coins
ans = 'yes'
coin = 0
while ans == "yes":
    ans = input("You have %d coins. Do you want another? " % (coin)).lower()
    coin += 1
    if ans == "no":
        print ("Bye!")
        break
## ==============================
