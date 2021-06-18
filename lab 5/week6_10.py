import pandas as pd
dataa=pd.read_excel(r'abc.xlsx',sheet_name=0)
datab=pd.read_excel(r'abc.xlsx',sheet_name=1)
datac=pd.concat([dataa,datab],axis=0)
print(datac)
datac=pd.concat([dataa,datab],axis=1)
print(datac)
