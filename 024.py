import numpy as np
array1, array2 = np.arange(6) , [6, 7, 8, 9, 10, 11] 
stackarray = np.hstack((array1, array2))
# hstack merge arrays
print(stackarray)