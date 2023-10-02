import pandas as pd



print("-----------------CREATING DATAFRAME FROM CSV------------------------")
csvDf = pd.read_csv("../resources/nba.csv", index_col="Name")
rowData = csvDf.loc["Avery Bradley"]

print(rowData)