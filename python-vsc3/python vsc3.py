import numpy as np

numberss = np.array([0,5,10,15,20,25,50,75])

result = numberss[::-1]

print(result)

numbers = np.array([[0,5,10],[15,20,25],[50,75,85]])
result1=numbers[-1,0:2]
print(result1)

arr1= np.arange(0,10)
arr2 = arr1.copy() 
arr2[0]=20
print(arr1)
print(arr2)