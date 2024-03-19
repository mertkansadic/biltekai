import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2

result = np.sqrt(numbers1)
print(result)

result1 = numbers1.reshape(2,3)
result2 = numbers2.reshape(2,3)
result3 = np.vstack((result1,result2))
print(result3)
check = numbers1 >50
print(check)