import matplotlib.pyplot as plt
import pandas as pd

excelDf = pd.read_excel("../resources/nba_excel.xlsx", index_col="EmpID")

head = excelDf.head(10)
# Sample data
x = head['Last Name']
y = head['Salary']

# Create a line plot
plt.figure(figsize=(14, 10))
plt.plot(x, y)

# Adding labels and a title
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Line Plot')

# Display the plot
plt.show()
