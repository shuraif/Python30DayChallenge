
file_path = '../resources/ProjectDetails.txt'  # Replace with the actual path to your text file
# Writing to a text file

lastLine = 0
with open(file_path, 'r') as file:
    for line in file:
        lastLine = line.strip()

with open(file_path, 'a') as file:
    if isinstance(int(lastLine), (int, float)):
        nextInt = int(lastLine)+1
        print(nextInt)
        file.write(str(nextInt)+"\n")