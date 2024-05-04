import pandas as pd
import numpy as np


data = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çinar",80]]

df = pd.DataFrame(data, index = [1,2,3,4],columns = ['Name','Grade'])

print(df)

dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}

df = pd.DataFrame(dict,index =["212","232","456","789"] )
print(df)


dict_list =[
    {"Name":"Ahmet","Grade":50},
    {"Name":"Ali","Grade":60},
    {"Name":"Yağmur","Grade":70},
    {"Name":"Çinar","Grade":0}]
df = pd.DataFrame(dict_list)
print(df)












"""s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)

print(df)"""
