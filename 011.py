s=0
array = []
lenth = int(input("enter lenth of array "))
i=0
while i < lenth :
    print("Enter the value of the ",i+1," value" )
    value = input()
    array.insert(i, value)
    i += 1

print(array)

for x in array :
    s= s+ int(x)

average = s/lenth
print("the average is",average)
