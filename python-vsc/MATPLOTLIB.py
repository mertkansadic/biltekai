import matplotlib.pyplot as plt
import numpy as np

"""x = np.array([0,6])
y = np.array([0,250])

plt.plot(x,y)
plt.show()"""

"""xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints,'o')
plt.show()"""
#plt.plot(birinci parametre,ikinci parametre,'o')

"""xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()"""

"""ypoints = np.array([3,8,1,10,5,7])
plt.plot(ypoints)
plt.show()"""
# x değerleri varsayan oluyor(0-5)

"""ypoints = np.array([3,8,1,10])
plt.plot(ypoints,marker='o')
plt.show()

xpoints = np.array([3,8,1,10])
plt.plot(xpoints,marker='*')
plt.show()"""
#pointer seçme

"""ypoints = np.array([3,8,1,10])

plt.plot(ypoints,'o:b')
plt.show()"""
# o =marker, : =line, r = color

"""ypoints = np.array([3,8,1,10])

plt.plot(ypoints, marker ='o', ms=100, mec='g',mfc="g")
plt.show()"""
#pointer boyutu ve rengi ms boyut için, mec kenar rengi
#mfc pointerın iç rengi

"""ypoints = np.array([3,8,1,10])

plt.plot(ypoints, linestyle='dashed')
plt.show()"""

"""ypoints = np.array([3,8,1,10])

plt.plot(ypoints, color='r')
plt.show()""" 
#grafik rengi

"""ypoints = np.array([3,8,1,10])

plt.plot(ypoints, linewidth='10')
plt.show()"""


"""y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])

plt.plot(y1)
plt.plot(y2)

plt.show()"""
#iki farklı grafiğin çizimi

"""x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

plt.plot(x1,y1,x2,y2)
plt.show()"""

"""x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)

plt.title("Sport Watch Date")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()"""

#baslık ve etiketler için yazı tipi özelliklerini ayarlayalım.
#loc = location
"""x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':'serif','color':'blue','size':20}

plt.title("Sport Watch Date",fontdict=font1,loc='left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y)
plt.show()"""







# Matplotlib sütun çizgileri ekleme #

"""x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burnage")

plt.plot(x,y)
plt.grid()  #sütun eklemek için
plt.show()"""




"""x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burnage")

plt.plot(x,y)
plt.grid(axis='x')  #tek bir ekseni belirtmek için
plt.show()"""


"""x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burnage")

plt.plot(x,y)
plt.grid(color='green',linestyle='--',linewidth=0.5)  #tek bir ekseni belirtmek için
plt.show()#sütun için özellikler
"""



#çoklu grafikleri görüntüleme

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
#ilk parametre satır
#ikinci değer sütun
#üçüncü parametre grafiğin indexi
plt.plot(x,y)
plt.title("Sales")

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Income")

plt.suptitle("MY SHOP")
plt.show()