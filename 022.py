array = []
lenth = int(input("enter lenth of array "))
i=0
while i < lenth :
    print("Enter the value of the ",i+1," value" )
    value = input()
    array.insert(i, value)
    i += 1
print(array)
i=0
reverse = [] # exit array
while i < lenth :
    reverse.insert(i,array[lenth -1- i]) # inverse filling, last value in array as first in reverse
    i+=1
print(reverse)