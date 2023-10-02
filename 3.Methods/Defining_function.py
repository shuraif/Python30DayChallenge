#for defining functions we can use keyword def

def readInput():
    num = int(input("Enter number"))
    return  num

def sum(num1,num2):
    return num1+num2

num1 = readInput()
num2 = readInput()
total = sum(num1,num2)

print("Sum : ",total)
