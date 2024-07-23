# good numbers:
import math
arr=[35,9,1]
count=0
res=0
for i in arr:
    low=1
    high=math.ceil(i**0.3)
    while low<high:
        res=low**3+high**3
        if res==i:
            count+=1
        low+=1
        print(i)
print('the count:',count)        