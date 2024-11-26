array = []
lenth = int(input("enter lenth of array "))
c=0
i=0
while i < lenth :
    print("Enter the value of the ",i+1," value" )
    value = input()
    array.insert(i, value)
    i += 1
print(array)

max = int(array[0])
while c < lenth : 
    if max < int(array[c]) :
        max = int(array[c])
    c += 1

print(max)