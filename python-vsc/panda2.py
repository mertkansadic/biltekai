import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns=["Columns1","Columns2","Columns3"])

result = df
result = df["Columns1"]
result = type(df["Columns1"])
result = df[["Columns1","Columns2"]]

result = df.loc["A"]
result = type(df.loc["A"])
#loc["row","column"] => loc["row"]=>loc[":","column"]
result = df.loc[:,["Columns1","Columns2"]]
result = df.loc[:,"Columns1":"Columns3"]
result = df.loc["A":"B",:"Columns2"]

"""result = df.iloc[2]"""

result = df.loc["A","Columns2"]
result = df.loc[["C","B"],["Columns1","Columns2"]]
print(result)


df["Columns4"] = pd.Series(randn(3),["A","B","C"])
df["Columns5"] = df["Columns1"] + df["Columns4"]

result = df.drop("Columns5",axis = 1, inplace = True)

print(df)
print(df.drop("Columns5",axis = 1))
print(result)