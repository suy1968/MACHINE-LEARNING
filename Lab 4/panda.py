import pandas as pd
data = pd.read_excel(r'abc.xlsx',sheet_name=0)
print(pd.DataFrame(data,columns=['Eno','Marks1']))
