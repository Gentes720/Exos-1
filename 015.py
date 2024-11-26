def Fibonacci(n):
    tab , i = [0,1] , 2
    if n == 1 :
        return 0
    elif n == 2:
        return 1
    else:
        while i < n:
            tab.insert(i, int(tab[i-1]) + int(tab[i-2]))
            i += 1
    return tab[n-1]

n = int(input("Enter the rank of the fibonacci number you want "))
print("the ", n," fibonacci number is ", Fibonacci(n))