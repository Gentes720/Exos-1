import numpy as np
def FistPprimeNum(n, p):
    def prime(x): # prime number tester function
        if x < 1:
            return False
        if x == 1:
            return True
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        max_divisor = int(np.sqrt(x)) + 1 # the square root of a number is it maximun dividor 
        for i in range(3, max_divisor, 2):
            if x % i == 0:
                return False
        return True
    
    array = np.zeros(p, dtype= int)

    i = n + 1 
    CountNumPrime = 0
    while CountNumPrime < p:
        if prime(i):
            array[CountNumPrime]= i
            CountNumPrime += 1
        i +=1

    print(array)

# test     
FistPprimeNum(3,4)