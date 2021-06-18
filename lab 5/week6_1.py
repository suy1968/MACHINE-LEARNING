import pandas as pd
data = pd.read_excel(r'abc.xlsx')
print(data.iloc[2])
print(data.loc[2])
print(data.iloc[1:4])
