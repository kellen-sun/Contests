n,k=map(int, input().split())
a=[tuple(map(int, input().split())) for i in range(n)]
a.sort(key=lambda x:x[1])
ans=0

for j in range(k):
    c=-1
    i=0
    while i<len(a):
        if a[i][0]>=c:
            ans+=1
            c=a[i][1]
            a.pop(i)
        i+=1
print(ans)
