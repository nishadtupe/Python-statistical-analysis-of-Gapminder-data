# Import Data Using Pandas.

# Import pandas library
import pandas as pd

# Assign spreadsheet filename: file
file = './Data/census.xlsx'

# Load spreadsheet: xl
S1 = pd.ExcelFile(file)

# Parse the first sheet and rename the columns: df
df = S1.parse(0, skiprows=[0], names=['Country', 'Avg_Age'])

# Print the head of the DataFrame df
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = Sl.parse(0, parse_cols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

## ------------------------ Using Numpy and Pandas loading txt files ----------------------------------##

import numpy as np
import matplotlib.pyplot as plt

# Assign filename: file
file = './Data/applications.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first 10 elements element of data
print(data[0:10])

# Import data as floats and skip the first row: data_float
np_data = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 6th element of data_float
print(np_data[5])

# Plot a scatterplot of the data
plt.scatter(np_data[:, 0], np_data[:, 1])
plt.show()