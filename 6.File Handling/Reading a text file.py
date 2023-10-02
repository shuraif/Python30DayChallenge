# Reading a text file
file_path = '../resources/ProjectDetails.txt'  # Replace with the actual path to your text file

with open(file_path, 'r') as file:
    content = file.read()  # Reads the entire file into a single string
    print(content)

print('------------------------------')