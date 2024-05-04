import pandas as pd

data ={
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,20,45,25],
    "Column3":["abc","bcaa","ade","cba","dea"]}
df = pd.DataFrame(data)

def kareal(x):
    return x*x

result = df
result = df["Column2"].unique()
result = df["Column2"].nunique()
result = df["Column2"].value_counts()
result = df["Column1"]*2
result = df["Column1"].apply(kareal) # def kareal(x)
df["Column4"] = df["Column3"].apply(len)
result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info


result = df.sort_values("Column2")
result = df.sort_values("Column3")
result = df.sort_values("Column3", ascending=False)


print(result)