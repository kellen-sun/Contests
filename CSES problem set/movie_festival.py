n=int(input())
a=[tuple(map(int, input().split())) for i in range(n)]
a.sort(key=lambda x:x[1])
c=-1
ans=0
for i in range(n):
    if a[i][0]>=c:
        ans+=1
        c=a[i][1]
print(ans)
