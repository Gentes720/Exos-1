
import numpy as np

def prime(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(np.sqrt(n)) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

# creation of an array of 100 element
array = np.zeros(100, dtype=int)

# Research of the 100 first prime numbers
count = 0
num = 1
while count < 100:
    if prime(num):
        array[count] = num
        count += 1
    num += 1

# results
print(array)
