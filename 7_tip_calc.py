# 7. tip calculator
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

# ========== first draft ==========
# bill = int(input("What is the total bill amount?"))
# tip = 0
# srv = input("Level of service? Good / Fair / Bad ").lower()

# if bill < 0:
#     print ("Type in proper bill amount.")
# else:
#     if srv == 'bad':
#         tip = bill * 0.1
#     elif srv == 'fair':
#         tip = bill * 0.15
#     elif srv == 'good':
#         tip = bill * 0.2

# print ('Tip amount ${:.2f} Total amount ${:.2f}'.format(tip, bill+tip))
