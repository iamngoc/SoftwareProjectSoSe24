import pandas as pd
import numpy as np
from pandas.core.interchange import column

#count child links for each parent link
df = pd.read_excel('Mappe1.xlsx', header=0, names=["Parent Link", "Child Link"])

child = df["Child Link"].values
print(child)

child = df["Child Link"].dtypes
print(child)