import pandas as pd
import numpy as np


#creating dataframe using list
print("-----------------CREATING DATAFRAME FROM ARRAY------------------------")
seq_arr = np.arange(0, 100, 7)
df = pd.DataFrame(seq_arr)
print(df)
print("-----------------CREATING DATAFRAME FROM LISTS------------------------")

data = {"Name":['john','David','Suja'],"Age":[30,45,83]}
dfData = pd.DataFrame(data)
print(dfData)

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

print("-----------------CREATING DATAFRAME FROM CSV------------------------")
csvDf = pd.read_csv("./resources/nba.csv", index_col="Name")
rowData = csvDf.loc["Avery Bradley"]
print(rowData)