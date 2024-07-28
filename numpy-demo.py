from audioop import maxpp
from multiprocessing import resource_tracker
from unittest import result
import numpy as np

result = np.array([10,15,30,45,60])

result = np.arange(5,15)

result = np.arange(50,100,5)

result = np.zeros(10)

result = np.ones(10)

result = np.linspace(0,100,5)

result = np.random.randint(10,30,5)

result = np.random.rand(10)

result = np.random.randint(10,50,15).reshape(3,5)

toplam1 = result.sum(axis=1) #yatay toplam

toplam2= result.sum(axis=0) #dikey toplam

max = result.max()
min = result.min()
ortalama = result.mean()

enBuyuk = result.argmax()

result = np.arange(10,20).reshape(2,5)
result = result ** 2

result = np.arange(-50,50)

ciftler = result[result %2 ==0] 
result = ciftler[ciftler>0]




print(result)


"""
print(max)
print(min)
print(ortalama)
"""