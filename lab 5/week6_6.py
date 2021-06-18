import pandas as pd
data = pd.read_csv('https://tinyurl.com/titanic-csv')
print(data['Age'].mean())
print(data['Age'].var())
print(data['Age'].kurt())
print(data['Age'].skew())
print(data['Age'].sem())
print(data['Age'].mode())
print(data['Age'].median())

