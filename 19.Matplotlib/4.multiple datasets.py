import matplotlib.pyplot as plt
import pandas as pd

excelDf = pd.read_excel("../resources/nba_excel.xlsx", index_col="EmpID")

head = excelDf.head(10)
# Sample data
x = head['Last Name']
y1 = head['Age']
y2 = head['Weight']

# Plot the first dataset (y1)
plt.figure(figsize=(14, 10))
plt.plot(x, y1, label='Age', color='blue', linestyle='-', marker='o')

# Plot the second dataset (y2)
plt.plot(x, y2, label='Weight', color='red', linestyle='--', marker='x')

# Adding labels and a legend
plt.xlabel('Name')

plt.title('Multiple Datasets on the Same Graph')
plt.legend()

# Display the plot
plt.show()
