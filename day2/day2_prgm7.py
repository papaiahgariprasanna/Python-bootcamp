n=int(input())
p=int(input())
time_remaining=240-p
count=0
for i in range (1,n+1):
    solve_time=i*5
    if solve_time<time_remaining and time_remaining>0:
        count+=1
        time_remaining-=solve_time
print(count)