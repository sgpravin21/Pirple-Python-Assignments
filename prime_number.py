'''
Homework Assignment #5: Basic Loops
assignment called "Fizz Buzz"
'''
# --FizzBuzz example--

# for i in range(1, 101, 1):
#     if(i%3 == 0 and i%5 == 0):
#         print(str(i) + " = FizzBuzz")
#     elif(i%3 ==0):
#         print(str(i) + " = Fizz")
#     elif(i%5 == 0):
#         print(str(i) + " = Buzz")
#     else:
#         print(i)

#========
# prime number
x = int(input("enter number: ")) #4
flag = "false"

if (x ==1 or x==2):
    print(str(x) + " is a prime number")
else:
    for i in range(2, x-1, 1):
        if(x % i == 0):
            print(str(x) + " is not prime number")
            flag = "true"
            break

if (flag == "false"):
    print(str(x) + " is a prime number")




