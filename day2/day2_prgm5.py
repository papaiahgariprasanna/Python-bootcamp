n=3
arr=[10,20,30]
total_cho_a=0
for num_of_chocolates in arr:
    total_cho_a+=(num_of_chocolates//3)
    if num_of_chocolates%3!=0:
        total_cho_a+=1
print(total_cho_a)