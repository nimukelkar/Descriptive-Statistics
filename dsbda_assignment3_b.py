
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df2=pd.read_csv('Iris.csv')
print(df2.head(10))

print(df2.describe())

df_setosa=df2[(df2["Species"]=="Iris-setosa")]
df_versicolor=df2[(df2["Species"]=="Iris-versicolor")]
df_virginica=df2[(df2["Species"]=="Iris-virginica")]

print("Summary statistics for Iris-setosa data group")
print(df_setosa.describe())

print("Summary statistics for Iris-versicolor group ")
print(df_versicolor.describe())

print("Summary statistics for Iris-virginica group")
print(df_virginica.describe())