import pandas as pd
import numpy as np
from pandas.core.interchange import column

#Read Excel Sheet
df = pd.read_excel('Mappe1.xlsx', header=0, names=["Parent", "Child"])

#count amount of links
count_rows = df[df.columns[0]].count()
print("number of rows: " , count_rows)

#convert to boolean-value sothat to count the links
list = pd.isnull(df['Parent'])
#print(list)

count = 0
arr_count = []

#count child links for each parent link
for i in list:
    if i == True:
        count += 1
    else:
        arr_count.append(count)
        count = 0

arr_count.append(count)
arr_count = arr_count[1:]
print(arr_count)

matrix = np.zeros([count_rows, count_rows])
#print(matrix)

#fill all the NaN values with '0'
df['Parent'] = df['Parent'].fillna(0)

#and convert from 'float64' to 'int64'
df['Parent'] = df['Parent'].astype(np.int64)

#do the same with column 'Child'
df['Child'] = df['Child'].fillna(0)
df['Child'] = df['Child'].astype(np.int64)

zeile_matrix = 0

#loop the column to read the velue
for i,row in df.iterrows():
    if df['Parent'][i] != 0:
        # - 1 for the index of matrix begins with 0
        spalte_matrix = df['Parent'][i] - 1
    else:
        zeile_matrix = df['Child'][i] - 1
        matrix[zeile_matrix][spalte_matrix] = 1 / arr_count[spalte_matrix]

print(matrix)
np.savetxt('matrix.txt', matrix, fmt = '%.2f')

print("Hello World")
