import pandas as pd
data = pd.read_csv('https://tinyurl.com/titanic-csv')
d1=data.drop('Age',axis=1)
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(d1.head())
print(data.head())
data.drop('Age',axis=1,inplace=True)
print(data)
