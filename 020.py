import numpy as np

array = np.arange(9).reshape(3, 3)
array_rotated = np.zeros(9).reshape(3, 3)
for i in range (0, 3):
    for x in range (0, 3):
       array_rotated[2 - x, i] = array[i, x]
# to rotate left a 3,3 array we iterate through the original array
# by fixing the row and incrementing the column,
# and through the modified array by fixing the column
# and decrementing the row from 2. Associating values at each step.
print(array[0,2])
print(array_rotated)