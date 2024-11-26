import math
phi = (1 + 5**0.5)/2
i = 0
while i < 10 :
    f = (phi**i-(1-phi)**i)/(5**0.5)
    print(round(f))
    i+= 1
