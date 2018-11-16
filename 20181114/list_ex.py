## ==============================
## 1 sum the numbers
lis = [1,16,18,19, 2050, 9.84, -10, 0]
sum = 0
for i in lis:
    sum += i
print (sum)

## ==============================
## 2 Larger Number
lis = [1,16,18,19, 2050, 9.84, -10, 0]
lis.sort()
print (lis[-1])

## ==============================
## 3 smallest Number
lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
lis.sort()
print (lis[0])

## ==============================
## 4 even number
lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
for i in lis:
    if i%2 == 0:
        print ("even number is :", i)

## ==============================
## 5 positive number
lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
for i in lis:
    if i > 0:  # 0 is not negative nor positive
        print ("positive number is :", i)

## ==============================
## 6 new list of positive number
lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
newlis =[]
for i in lis:
    if i > 0:  # 0 is not negative nor positive
        newlis.append(i)
print (newlis) # result not sorted

## ==============================
## 7 Multiply a list
lis = [1,16,18,19, 2050, 9.84, -10, 0, 0.5]
num = int(input("Type in a number: ")) # factor number
multiplyNum = []
for i in lis:
    multiplyNum.append(i * num)
print (multiplyNum)

## ==============================
##8 Multiply Vectors
list1 = [1,2,3]
list2 = [4,5,6]
pairList = []
for i in range(len(list1)): # as 2 lists are same length, loop by index
    pairList.append(list1[i] * list2[i])
print (pairList)

## ==============================
##9 & 10 Matrix Addition
##======= #10 worked on my solution for #9======
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
alist = [1,2,3,"ab","cd",3,"ab","one", "two", "one"]
newList = [alist[0]]
# loop all the element in a list
for ele in alist:
	if ele not in newList: newList.append(ele)
print (newList)

# Bonus: Matrix Multiplication
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. 
# Print the resulting matrix. How do you multiple two matricies? https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro
mxList1 = [[[1,2],[3,4]],[[5,6],[7,8]]]
mxList2 = [[[9,10],[11,12]],[[13,14],[15,16]]]
ansList = []

mxList1[[0][0][0]] * mxList2[[0][0][0]] + mxList1[[0][0][1]] * mxList2[[1][0][0]] 
mxList1[[0][1]] * mxList2[[0][0][1]] + mxList1[[0][1][1]] * mxList2[[1][0][1]] 
mxList1[[1][0][0]] * mxList2[[0][1][0]] + mxList1[[1][0][1]] * mxList2[[1][1][0]] 
mxList1[[0][0][0]] * mxList2[[0][1][1]] + mxList1[[1][1][1]] * mxList2[[1][1][1]] 