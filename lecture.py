# # # this is python exercise.
# # # I want to double check on commit.
# # #One more time oiajsieajwieawihf
# # #"Another test"

# # l1 = [1,5,3,6,7]
# # l2 = [3,6,9,10,2]
# # l3 = []

# # for i in l1:
# #     sum = 0
# #     #print (sum)
# #     for j in l2:
# #         sum += i * j
# #         # print ("outerloop:",i, "innerLoop:",j, "Total:", sum)
# #     l3.append(sum)
# # print (l3)

# # for x in range(-3, 5):
# #   print("f({x})={y} \t g({x})={z}".format(x=x, y=f(x), z=g(x))) 

# # a = "string"
# # b = [1,2,3,4,5]

# # def someFunc(a,b):
# #     a = "@string"
# #     b[0] = 0
# #     print (a)
# #     print(b)

# # someFunc(a,b)
# # print(a)
# # print(b)

# #=20181115========
# # import matplotlib
# # matplotlib.use("Agg")
# # from matplotlib import pyplot


# # def f(x):
# #   return 2 * x + 1

# # def g(x):
# #   return x + 1

# # f_output = []
# # g_output = []

# # x_list = list(range(-3, 5))
# # for x in x_list:
# #   f_output.append(f(x))
# #   g_output.append(g(x))

# # pyplot.plot(x_list, f_output, x_list, g_output)

# # pyplot.savefig('myplot.png')
# # pyplot.close() # start a new plot

# # xr = 10
# # for x in range(0, xr):
# #     space = xr-x-1
# #     start = x * 2+1
# #     print('' * spaces + '*' * starts)


# myContactList = {
#     "first_name": "Veronica",
#     "last_name" : "Lino",
#     "age": 12,
#     12: "street",
#     "friends": {
#         "frist_name": "Myname",
#         "last_name": "LastName",
#         "occupation": "student"
#     }
# }
# #first_name = myContactList["fog"]
# first_name = myContactList.get("fog")
# print ("dog" in myContactList)

# if "dog" in myContactList:
#     print ("Yay")
# else:
#     print ("Where is my dog?")


# for key, value in myContactList.items():
#     print ("{key}-{value}".format(key = key, value = value))

import pickle
data = {"name": "Paul"}
with open('data.picke', 'wb') as fh:

import jason
# import file in a same way wiht json