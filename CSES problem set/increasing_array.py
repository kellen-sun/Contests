input()
a=list(map(int, input().split()))
m=0
for x in range(len(a)-1):
    if a[x]>a[x+1]:
        m+=a[x]-a[x+1]
        a[x+1]=a[x]
print(m)
