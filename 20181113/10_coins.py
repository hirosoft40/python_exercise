# 10. coins
ans = 'yes'
coin = 0
while ans == "yes":
    ans = input("You have %d coins. Do you want another? " % (coin)).lower()
    coin += 1
    if ans == "no":
        print ("Bye!")
        break

