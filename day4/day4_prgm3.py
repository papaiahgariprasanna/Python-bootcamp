s='a1b2c3d492nm45'
# op=12349245abcdnm
s1=''
s2='' 
for i in s:
    if i.isdigit():
        s1+=i
    else:
        s2+=i
print(s1,s2)