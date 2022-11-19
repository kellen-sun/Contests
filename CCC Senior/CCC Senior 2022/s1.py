n = int(input())
s=0
c=0
while s<=n:
    if (n-s)%5==0:
        c+=1
    s+=4
print(c)
