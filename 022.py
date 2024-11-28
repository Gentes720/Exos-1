import numpy as np

array = np.arange(10).reshape(1,10)
i=0
reverse = np.empty( (1, 10) ) # exit array
while i < 10 :
    reverse[0, i] = array[0, 10 -1- i] 
    # inverse filling, last value in array as first in reverse
    i+=1
print(reverse)