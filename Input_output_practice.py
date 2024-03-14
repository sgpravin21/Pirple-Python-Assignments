# x = open('c:\\one\\news.txt', 'r')
#
# print(x.read())
#
# x.close()
#
# x = open('c:\\one\\news.txt', 'w')
#
# latest_news = "\n No, you cannot actually add a list to a set since lists are mutable and unhashable objects, and sets are immutable and do not accept unhashable objects."
#
# x.write(latest_news)
# x.close()
#
# x = open('c:\\one\\news.txt', 'r')
#
# print(x.read())

#-----------------------

# for i in range(1,5):
#     with open("c:\\one\\places" + str(i) + ".txt", "r") as x:
#         for line in x:
#             print(line)

#-----------------------
#this file take the data from 4 text files and combine into 1 text file
# for i in range(1,5):
#     x = open('c:\\one\\places' + str(i) + ".txt", 'r')
#     if i == 1 :
#         y = open('c:\\one\\places_all.txt', 'w')
#     else:
#         y = open('c:\\one\\places_all.txt', 'a')
#
#     a = x.read()
#     y.write(a)
#     #print(x.read())
#     x.close()
#     y.close()
#-----------------------
# txt = "welcome"
# print(txt[::-1])
# print(txt[::-1].capitalize())
#
# leng = len(txt)
# print(leng)
#
# for i in range(leng,0,-1):
#     print(i, end='')

# i = 1
# while(i <= leng):
#     print(i , end='')
#     i += 1
#
# for i in txt:
#     print(i, end='')
#---------------------------
#reverse string
# txt = input("enter text which need to be reverse :\n")
#
# def rev(input_txt):
#     output = input_txt
#     return(output[::-1])
#
# txt_rev = rev(txt)
# print(txt_rev)
#---------------------------

# str = "pravin india 50"
# str1 = str.split()
# print(str1)

file = open("c:\\one\\news.txt")
