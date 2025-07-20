num1 = int(input("Num1: \n"))
num2 = int(input("Num2: \n"))
num3 = int(input("Num3: \n"))

if(num1 > num2):
    if(num1 > num3):
        print(num1, "é o maior \n")
    elif(num3 > num2):
        print(num3, "é o maior \n")
elif(num2 > num3):
    print(num2, "é o maior \n")
else:
    print(num3, "é o maior \n")