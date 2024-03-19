import numpy as np

#result= np.array([1,3,5,7,9])
#result = np.arange(1,10)
result = np.arange(10,100,3)
#values for float zeros and ones 
result1= np.zeros(10)
result1=np.ones(9)
print(result1)
print(result)
#result2= np.linspace(0,100,5)
result2 = np.linspace(0,5,5)
print(result2)
result3 = np.random.randint(0,20)
#result3 = np.random.randint(20) same as above
print(result3)
result4= np.random.randint(1,10,3)
print(result4)

result5=np.random.randn(5)
#result5=np.random.rand(5)
print(result5)


np_array= np.arange(50)
result6 = np_array.reshape(5,10)
print(result6)
print(result6.sum(axis=1))
print(result6.sum(axis=0))


rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
#result7= rnd_numbers.max()
#result7= rnd_numbers.min()
#result7= rnd_numbers.mean()
#result7 = rnd_numbers.argmax()
result7= rnd_numbers.argmin()
print(result7)