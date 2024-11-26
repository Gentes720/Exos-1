string = input('enter the string to be reversed ')
array = []
for letter in string:
    array.append(letter)
lenth = len(array)
i=0
reverse = [] # exit array
while i < lenth :
    reverse.insert(i,array[lenth -1- i]) # inverse filling, last value in array as first in reverse
    i+=1
print("".join(reverse))