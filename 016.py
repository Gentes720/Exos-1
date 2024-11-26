def prime(number):
    i , c = 1 , 0
    while i < number/2 :
        if number % i == 0:
            c += 1
        i += 1
    if c == 1:
        return True
    else : 
        return False

number = int(input("Enter a number "))
if prime(number):
    print("it's a prime number")
else :
    print("it's not prime")