
#Name:-Nirmayi Kelkar
#Assignment3 on the nbs data set.

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

pd.set_option('display.float_format',lambda x:'%.2f'%x)

#Reading csv into the data frame.
df1=pd.read_csv('nba.csv')

#Printing out the first 10 records.
print(df1.head(10))

# Standard data pre processing.

#df1.replace("?",np.nan,inplace="True")


#Removing the records that have null values.
df1=df1.dropna()
print("After removing the null values, data shape is",df1.shape)
print("After removing nulls, head print",df1.head(10))


print(df1["Age"].describe())
dfl_25=df1[(df1["Age"]<25)]
df_25_30=df1[(df1["Age"]>=25) & (df1["Age"]<30)]
df_30_35=df1[(df1["Age"]>30) & (df1["Age"]<35)]
df_gt_35=df1[(df1["Age"]>35)]

print("\n Summary Stats for <25 Age Group")
print(dfl_25["Salary"].describe())
print("\n Summary Stats for between 25 and 30 Age Group")
print(df_25_30["Salary"].describe())
print("\n Summary Stats for between 30 and 35 age group")
print(df_30_35["Salary"].describe())
print("\n Summary Stats for above 35 age group")
print(df_gt_35["Salary"].describe())










