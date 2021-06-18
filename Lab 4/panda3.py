import pandas as pd
url = 'https://tinyurl.com/yx3b6sq3'
data = pd.read_csv(url,sep=';',header=None,prefix='Column',usecols=[1,3,4],skiprows=lambda x:x%2==0)
print(data)
