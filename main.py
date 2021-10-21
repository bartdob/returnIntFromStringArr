import requests
import numpy as np
import pandas as pd
import re


r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
print(len(r.json()['data']))

data = r.json()['data']
print(data)

print (data.count("age"))

f = data.find('age')
print(data[f+4] + data[f+5])
print(data[(f+4)+19] + data[(f+5)+19])

age = (re.findall(r'\d+', data))
print(age)
counter = 0
tab =[]

for s in age:
    tab.append(int(s))

print (tab)

for i in tab:
    if i >= 50:
        counter = counter+1

print(counter)
