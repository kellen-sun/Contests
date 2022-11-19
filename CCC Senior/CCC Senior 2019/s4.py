a=list(map(int,input().split()))
n=a[0]
k=a[1]
a=list(map(int,input().split()))

if len(a[:k])==0:
    u=0
else:
    u=max(a[:k])
if len(a[k:])==0:
    i=0
else:
    i=max(a[k:])
if len(a[:-k])==0:
    o=0
else:
    o=max(a[:-k])
if len(a[-k:])==0:
    p=0
else: 
    p=max(a[-k:])
print(max([u+i,(o+p)]))
