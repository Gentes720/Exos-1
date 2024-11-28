import numpy as np
array1, array2 = np.arange(6), [2, 4, 7, 5,8 ,9]
print(array1)
print(array2)
stackArray = np.hstack((array1, array2))
print(stackArray)
print(np.unique(stackArray))
# unique automaticaly delete repeated values in an array

