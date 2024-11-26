def prime(number):
    i , c = 1 , 0
    while i <= number/2 :
        if number % i == 0:
            c += 1 # c changes when there is at least one number different from 1 and number which is a divider of number
        i += 1
    if c == 1:
        return True
    else : 
        return False

CountNumPrime = 0
while CountNumPrime < 100 :
    for i in range(1, 560, 1):
        if prime(i):
            print(i)
            CountNumPrime += 1
    