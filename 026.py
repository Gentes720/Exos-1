import numpy as np
array1, array2 = np.arange(6), [2, 4, 7, 5,8 ,1]
print(array1)
print(array2)

uniqueArray = np.empty((1, 6))
for element in array1:
    if element not in array2:
        uniqueArray = np.append(uniqueArray, element)
print(uniqueArray)

