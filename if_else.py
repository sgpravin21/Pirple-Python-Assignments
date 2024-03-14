'''
this program will check the if the given numbers are equal or not
'''

# a,b,c = 11,20,"10" #This will print Two numbers are equal
# # a,b,c = 11,20,"10" #This will print All the numbers are different
#

def ThreeNums(a,b,c):
    if (a == b or a == int(c)):
        print("Two numbers are equal")
    elif (b == int(c)):
        print("Two numbers are equal")
    else:
        print("All the numbers are different")

#This function will print -> Two numbers are equal
ThreeNums(10,20,"10")

#This function will print -> All the numbers are different
ThreeNums(11,20,"10")


