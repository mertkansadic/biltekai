import pandas as pd
import numpy as np

numbers = [20,30,40,50]
letters = ["a","b","c","d"]
scalar = 5
pandas_series = pd.Series(scalar,[0,1,2,3,4])
pandas_series = pd.Series(scalar,["s","j","k","j","j"])

random_numbers=np.random.randint(10,100,6)

"""print(pandas_series)
print(pd.Series(random_numbers))"""

pandas_series=pd.Series([20,30,40,51],["a","b","c","f"])
result = pandas_series.ndim
result = pandas_series.dtype
result = pandas_series.shape
result = pandas_series.max()
result = pandas_series.min()
result = pandas_series.sum()
result = pandas_series + 50
result = pandas_series % 2 ==0
print(pandas_series[pandas_series % 2 ==0])

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

total = opel2018+opel2019

print(total["astra"])