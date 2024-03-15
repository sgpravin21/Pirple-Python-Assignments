#this funciton take the user input and write it to text file "c:\one\input_devices.txt"

iput_devices = open("c:\one\input_devices.txt", "w")

temp = ""

for i in range(3):
    user_input = input("enter input devies:\n")
    if i == 0:
        temp = user_input
    else:
        temp = temp + " , " + user_input

    user_input = ""

text = iput_devices.write(temp)
iput_devices.close()

print("input devices entered are entered into the text file")


