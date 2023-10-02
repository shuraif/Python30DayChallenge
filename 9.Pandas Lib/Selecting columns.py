import pandas as pd

print("------------------SELECTING COLUMNS-----------------------")

# Define a dictionary containing employee data
employeeData = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
empDf = pd.DataFrame(employeeData)

# select two columns
print(empDf[['Name', 'Qualification']])