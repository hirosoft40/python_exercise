# 5. Work or Sleep In?
day = int(input("Day (0-6)?"))
if day < 0 or day > 6:
    print ("Type in number between 0 to 6.")
elif day > 0 and day < 6:
    print ("Go to work!!")
else:
    print ("Sleep in.")
