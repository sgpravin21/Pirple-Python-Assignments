'''
Homework Assignment #4: Lists
'''

myUniqueList = []
myLeftovers = []
count = 0
flag = "no"

for i in range(0,5):
    x = input("Enter any 5 Numbers: ")
    if i == 0:
        myUniqueList.append(x)
    else:
        for y in range(0, len(myUniqueList)):
            if x == myUniqueList[y]:
                flag = "yes"
                myLeftovers.append(x)
                continue
        if flag == "no":
            myUniqueList.append(x)

print("Unique list is : " + str(myUniqueList))
print("Left over numbers : " + str(myLeftovers))