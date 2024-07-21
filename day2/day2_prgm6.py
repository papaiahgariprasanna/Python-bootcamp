N=1895
def digit_sum(num):
    total=0
    while num>0:
        total+=num%10
        num//=10
    return total
while N>9:
    N=digit_sum(N)
print(N)