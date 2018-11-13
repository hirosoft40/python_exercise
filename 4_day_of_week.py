#4. Day of the week
day = int(input('Day (0-6)? '))
week = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}
if day in week.keys():
    print (week[day])
else:
    print ("Type in number between 0 to 6!")

"""
===== initial solution for No.4 ========
day = int(input('Day (0-6)? '))
if day < 0 or day >=7:
    print ('Type in number between 0 to 6!')
elif day == 0:
    print ('Sunday')
elif day == 1:
    print ("Monday")
elif day == 2:
    print ("Tuesday")
elif day == 3:
    print ("Wednesday")
elif day == 4:
    print ("Thursday")
elif day == 5:
    print ("Friday")
elif day == 6:
    print ("Saturday")
else:
    print ("Something is horribly wrong!")
"""
