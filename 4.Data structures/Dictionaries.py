# Creating a Dictionary:
# To create a dictionary, you can use curly braces {} and specify key-value pairs separated by colons :. For example:

myDict = {"name": "John", "age": 30, "city": "New York"}
print(myDict)
name =myDict["name"]
print("Name : ",name)

print("Age :",myDict.get("age"))

#Modifying a Dictionary:

myDict["age"] = 31  # Updating a value
myDict["country"] = "USA"  # Adding a new key-value pair
del myDict["city"]  # Removing a key-value pair

print(myDict)

# Dictionary Methods:
# Python provides various methods for working with dictionaries, including:
#




print("keys(): Returns a list of all keys in the dictionary.")
for key in myDict.keys():
    print(key,":",myDict[key])

print("values(): Returns a list of all values in the dictionary.")
for value in myDict.values():
    print(value)

print("items(): Returns a list of key-value pairs as tuples.")
for item in myDict.items():
    print(item)

print("pop(key): Removes the key and its associated value from the dictionary.")
myDict.pop("name")
print(myDict)

print(" popitem(): Removes and returns an arbitrary key-value pair.")
popedItem = myDict.popitem()
print(popedItem)

#Python supports dictionary comprehensions for creating dictionaries in a concise manner:
squares = {x: x**2 for x in range(11)}
print(squares)