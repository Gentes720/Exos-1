def FistPprimeNum(n, p):
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

    i = n + 1 
    CountNumPrime = 0
    while CountNumPrime < p:
        if prime(i):
            print(i)
            CountNumPrime += 1
        i +=1

FistPprimeNum(3,4)