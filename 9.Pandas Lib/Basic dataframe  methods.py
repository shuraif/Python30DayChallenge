import pandas as pd


print("-----------------Basic dataframe  methods----------------------")

excelDf = pd.read_excel("../resources/nba_excel.xlsx", index_col="EmpID")


print(excelDf[0:3])

player = excelDf.loc["U143442"]
print(player)

print("Length of dataframe: ",len(excelDf.index))

print("head 5")
print(excelDf.head(5))

print("-----Statistics----")
print(excelDf.describe())

print("----info----")
print(excelDf.info)


