arr=[1,2,3,4,5,4,3,6]
count=0
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for num,count in d.items():
    if count==1:
        print(num)
