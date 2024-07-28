import numpy as np

#pyhton list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy list
np_array = np.array(py_list)

np_multi = np_array.reshape(3,3)

print(py_list)
print(np_array.shape)
print(np_multi.shape)

