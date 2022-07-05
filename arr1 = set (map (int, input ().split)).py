import pandas as pd
from collections import Counter

data = pd.read_csv(r'E:\курсы\DS\[Нетология] Профессия - Data Scientist (2018)\01. Подготовка\DZ1\urls.txt',)
print (data)
data = data.values.tolist()
list = []
sep_list = []
for i in data:
    list += i
for i in list:
    sep_list += i.split("/")
print( Counter( sep_list ).keys() ) # equals to list(set(words))
print( Counter( sep_list ).values() ) # counts the elements' frequency



        