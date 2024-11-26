
def positive(array) :
    i = 0
    while i < len(array)  :
        if int(array[i]) < 0 :
            del(array[i])
        i +=1
    return array

array = []
lenth = int(input("enter lenth of array "))
i=0
while i < lenth :
    print("Enter the value of the ",i+1," value" )
    value = input()
    array.insert(i, value)
    i += 1
print(array)

print(positive(array))