import pandas as pd
import numpy as np
from pandas.core.interchange import column

#define a scalar between 0 and 1
alpha = 0.9

#Read Excel Sheet
df = pd.read_excel('test2.xlsx', header=0, names=["Parent", "Child"])

#count amount of links
count_rows = df[df.columns[0]].count()
#print("number of rows: " , count_rows)

#create an integer vector e and e_transpose has length(count_rows) with 1s
e = np.ones(count_rows, dtype=int)
e_T = np.array([e]).T

#convert to boolean-value so that to count the links
list = pd.isnull(df['Parent'])

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

#delete the first value because the main link included
arr_count = arr_count[1:]
#print(arr_count)

matrix = np.zeros([count_rows, count_rows])
#print(matrix)

#fill all the NaN values with '0'
df['Parent'] = df['Parent'].fillna(0)

#and convert from 'float64' to 'int64'
df['Parent'] = df['Parent'].astype(np.int64)

#do the same with column 'Child'
df['Child'] = df['Child'].fillna(0)
df['Child'] = df['Child'].astype(np.int64)

spalte_matrix = 0

#loop the column to read the value not 0
for i,row in df.iterrows():
    if df['Parent'][i] != 0:
        # - 1 for the index of matrix begins with 0
        zeile_matrix = df['Parent'][i] - 1
    else:
        spalte_matrix = df['Child'][i] - 1
        matrix[zeile_matrix][spalte_matrix] = 1 / arr_count[zeile_matrix]

#function for vector a is a dangling node and 0 otherwise
def dangling_node_vector(matrix, count_rows):
    y = np.zeros(count_rows, dtype=int)
    for i in range(count_rows):
        if sum(matrix[i]) == 0:
            y[i] = 1
    return y

#function replaces the O_T rows with 1/n * e_T
def stochastic_matrix(matrix, count_rows):

    for i in range(count_rows):
        if sum(matrix[i]) == 0:
            matrix[i] = 1 / count_rows
    return matrix

vec_a = dangling_node_vector(matrix, count_rows)

stochastic_matrix(matrix, count_rows)

g_matrix = alpha * matrix + (1 - alpha) * (1 / count_rows) * e * e_T
print(g_matrix)
np.savetxt('matrix_test.txt', g_matrix, fmt = '%.5f')