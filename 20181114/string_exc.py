somestr = input("Type in some message.")
## ==============================
## 1 Change to uppercase
print (somestr.upper())

## ==============================
## 2 Capitalizing 
print (somestr[0].upper() +somestr[1:] ) 

## ==============================
## 3 Reverse letters 
print (somestr[::-1]) 

## ==============================
## 4 Leetspeak
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
for i in somestr.upper():
    if i in leet.keys():
        msg += leet[i].lower()  # per sample, changed to lowercase.
    else:
        msg += i.lower() # per sample, changed to lowercase.
print (msg)

## 5 long-long vowels
## test case: good, nachocheese, spoon, food, eat, soup, 
## ????? NOT FINISHED for nahcocheese. and I feel these are nested too much.
longV = input("What is your favorite long vowel word?: ")
vow = ('a','e','i','o','u') # vowels tuple 
veryLongV = ""     # string to hold loooong vowel
vowCount = 0       # count how many vowels in word input by user

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
print (newMsg)