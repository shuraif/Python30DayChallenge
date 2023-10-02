
file_path = '../resources/ProjectDetails.txt'  # Replace with the actual path to your text file
# Reading a text file line by line
lastLine = 0
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())  # Use strip() to remove leading/trailing whitespace
        print('------------------------------------------------------------')
        lastLine = line.strip()