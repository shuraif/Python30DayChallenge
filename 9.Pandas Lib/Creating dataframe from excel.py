import pandas as pd

print("-----------------CREATING DATAFRAME FROM EXCEL-----------------------")

excelDf = pd.read_excel("../resources/nba_excel.xlsx", index_col="EmpID")
#print(excelDf)

print(excelDf[0:3])