# Reading a text file
file_path = 'resources/ProjectDetails.txt'  # Replace with the actual path to your text file

with open(file_path, 'r') as file:
    content = file.read()  # Reads the entire file into a single string
    print(content)

print('------------------------------')


# Reading a text file line by line
lastLine = 0
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())  # Use strip() to remove leading/trailing whitespace
        print('------------------------------------------------------------')
        lastLine = line.strip()

print('------------------------------')

# Writing to a text file
with open(file_path, 'a') as file:
    if isinstance(int(lastLine), (int, float)):
        nextInt = int(lastLine)+1
        print(nextInt)
        file.write(str(nextInt)+"\n")

