import pandas as pd
url='https://tinyurl.com/yx3b6sq3'
data=pd.read_csv(url,sep=';',header=None,prefix='Column')
print(data[(data['Column1']==0.580) & (data['Column4']==1)])
