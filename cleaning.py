import pandas as pd


data = pd.read_csv('data.csv')

data.to_excel('df.xlsx',index=False)