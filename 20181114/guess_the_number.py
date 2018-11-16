# 2018/11/14 Guess a number game
import random 

# === guess the number 
#===============================================
# Step1: hard code number 
#===============================================

num = 5 # secret number
count = 5
print ("I am thinking of a number between 1 and 10.")
user_num = int(input("What's the number? : "))

while num != user_num:
     # when number is way off, shows error.
    if user_num > 10 or user_num < 0:
        print ("Type in number between 1 and 10. ")
    else:
        print ("Nope, %d is not right. Try again." % user_num)
    # Prompt user same question. should be functionized.  
    user_num = int(input("What's the number? : "))

#Loop out when number matches.
print ("Yes, you won!")

# #===============================================
# # Step2: Give low and high
# #===============================================
num = 5 # secret number
count = 5
print ("I am thinking of a number between 1 and 10. ")
user_num = int(input("What's the number? : "))

while num != user_num:
    # when number is way off, shows error
    if user_num > 10 or user_num < 0:
        print ("Type in number between 1 and 10. ")
    # if the number is 2 or more away, the messages shows either too high/too low
    elif user_num > num + 1: 
        print("Nope, %d is too high." % user_num)
    elif user_num < num - 1:
        print ("Nope, %d is too low." % user_num)
    # if the number is 1 different, "close" message displays
    else:
        print ("Nope, %d is close." % user_num)
    print ("Try again.")
    user_num = int(input("What's the number? : "))

# Loop out when number matches.
print ("Yes, you won!")

# #===============================================
# # Step3: random
# #===============================================

num = random.randint(1,10) # generating random number

# initial intract with user.
print ("I am thinking of a number between 1 and 10.")
user_num = int(input("What's the number? : "))

while num != user_num:
    if user_num > 10 or user_num < 0:
        print ("Type in number between 1 and 10. ")
    elif user_num > num + 1: 
        print("Nope, %d is too high." % user_num)
    elif user_num < num - 1:
        print ("Nope, %d is too low." % user_num)
    else:
        print ("Nope, %d is close." % user_num)
    user_num = int(input("What's the number? : "))

print ("Yes, %d is the number! You won!" % user_num)

# #===============================================
# # Step4: Limit number of guesses
# #===============================================

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
    

# #===============================================
# # Bonus: Play again
# #===============================================
# # Problems to be fixed: Currently can play only for 2 times continuously.

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
        
# calling function guess
guess()

# continue or not
again = input("Do you want to play again? (Y or N)").lower()
if again == 'y':
    guess()
else:
    print ("Good bye. See you soon.")
