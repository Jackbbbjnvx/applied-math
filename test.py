x= int(input("What is the value of X?: \n"))
y= int(input("What is the value of Y?: \n"))


value = 1

while(value):
    z = input('''what do you want to do?
    To add x and y press A and Enter
    To subtract x and y press S and Enter
    To multiply x and y press M and Enter
    To divide x and y press D and Enter: \n''')

    if z != "A" or z != "A" or z != "A" or z != "A":
        print("Please enter valid command \n")
    exit
    if z == "A":
        print(x+y)

    elif z == "S":
        print(x-y)

    elif z == "M":
        print(x*y)

    elif z == "D":
        print(x/y)
