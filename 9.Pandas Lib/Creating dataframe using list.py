import pandas as pd

print("-----------------CREATING DATAFRAME FROM LISTS------------------------")
data = {"Name":['john','David','Suja'],"Age":[30,45,83]}
dfData = pd.DataFrame(data)
print(dfData)