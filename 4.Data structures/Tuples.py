myTuple = (12,45,76,56)
print("------Printing-------")
print(myTuple)
print("----Printing with for each loop---------")

for tup in myTuple:
    print(tup)
print("------Print with iteration-------")

for i in range(0, len(myTuple)):
    print(myTuple[i])

print("------Printing after unpacking elements-------")
fst,sec,thrd,fourth = myTuple
print(fst,sec,thrd,fourth)

print("------Printing sliced tuple-------")
subTuple = myTuple[1:3]
print(subTuple)

print("------Printing concatinated tuple-------")
myTuple+=subTuple
print(myTuple)


print("------Printing repeated tuple-------")
subTuple*=5
print(subTuple)

choice = int(input("enter choice : "))
if(choice in myTuple):
    print("item found")
else:
    print("item not found")

print("--------nested tuple---------")
nested_tuple = (10, (20, 83), 4)
print(nested_tuple)


print("--------nested tuple with for loops---------")
for i in range(0, len(nested_tuple)):
    if isinstance(nested_tuple[i],tuple):
        for k in range(0,len(nested_tuple[i])):
            print(nested_tuple[i][k])
    else:
        print(nested_tuple[i])



