globalVar = 10

def modifyGlobal():

    global globalVar
    print("Global var before modifying",globalVar)
    globalVar+=30
    print("Global var after modifying",globalVar)

modifyGlobal()
print(globalVar)
