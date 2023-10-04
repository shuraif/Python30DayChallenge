import matplotlib.pyplot as plt
import pandas as pd

excelDf = pd.read_excel("../resources/nba_excel.xlsx", index_col="EmpID")

head = excelDf.head(10)
# Sample data
x = head['Last Name']
y = head['Age']

# Create a scatter plot
plt.figure(figsize=(14, 10))
plt.bar(x, y)

# Adding labels and a title
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Scatter Plot')

# Display the plot
plt.show()
