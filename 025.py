array1, array2 = [], []
lenth1 = int(input("enter lenth of array1 "))
i=0
while i < lenth1 :
    print("Enter the value of the ",i+1," value" )
    value = input()
    array1.insert(i, value)
    i += 1
print(array1)
lenth2 = int(input("enter lenth of array2 "))
i=0
while i < lenth2 :
    print("Enter the value of the ",i+1," value" )
    value = input()
    array2.insert(i, value)
    i += 1
print(array2)
array1.extend(array2)
print(array1)

uniqueArray = []
for element in array1:
    if element not in uniqueArray:
        uniqueArray.append(element)
print(uniqueArray)

