import pandas as pd
data = pd.read_excel(r'abc.xlsx')
print(data.drop_duplicates())
print(data)
d1=data.drop_duplicates()
print(d1)
d2=data.drop_duplicates(subset=['Marks1'])
print(d2)
