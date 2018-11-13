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


# #===================== first try ===========
# # 8. tip calculator2
# bill = int(input("What is the total bill amount?"))
# srv = input("Level of service? Good / Fair / Bad ").lower()
# spl = int(input("How many ways? Tyep in number."))
# tip = 0

# if bill < 0 or spl < 1:
#     print ("Type in proper number.")
# else:
#     if srv == 'bad':
#         tip = bill * 0.1
#     elif srv == 'fair':
#         tip = bill * 0.15
#     elif srv == 'good':
#         tip = bill * 0.2
    
# print ('Tip amount ${:.2f} Total amount ${:.2f}'.format(tip, bill+tip))
# print ('Amount per person: ${:.2f}'.format((bill + tip)/spl))
 