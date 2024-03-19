import numpy as np

# 1-(10,15,30,45,60) değerlerine saship numpy dizisi oluşturunuz.
arr1 = np.array([10,15,30,45,60])
print(arr1)

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
arr2=np.arange(5,15)
print(arr2)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
arr3 = np.arange(50,100,5)
print(arr3)

# 4-10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
arr4 = np.zeros(10)
print(arr4)

# 5-10 elemanlı birlerden oluşan bir dizi oluşturunuz.
arr5 = np.ones(10)
print(arr5)

#6- (0-100) arasında eşit aralıklı 5 sayı üretin.
arr6 = np.linspace(0,100,5)
print(arr6)

#7 - (10-30) arasında rastgele 5 tane tamsayı üretin.
arr7 = np.random.randint(10,30,5)
print(arr7)

#8- [-1 ile 1] arasında 10 adet sayı üretin
arr8= np.random.randn(10)
print(arr8)

#9-(3X5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
arr9 = np.random.randint(10,50,15)
arr9 = arr9.reshape(3,5)
print(arr9)

rowTotal = arr9.sum(axis =1)
colTotal = arr9.sum(axis = 0)
print(rowTotal)
print(colTotal)

# 10- üretilen matrisin en büyük, en küçük ve ortalaması nedir?
minm= arr9.min()
maxm= arr9.max()
averagem= arr9.mean()
print(averagem)

# 11- üretilen matrisin en büyük değerinin indeksi kaçtır?
arr9=np.random.randint(50,100,15)
maxm = arr9.argmax()
print(arr9)
print(maxm)

# 12- üretilen matrisin her bir elemanının karesini alınız.
result = arr9 ** 2
print(result)


# 13- pozitif çift sayıları buldur.
arr = np.random.randint(-50,50,50)
result = arr[arr%2==0]
result = result[result>0]
print(result)

