n=int(input())
a=[tuple(map(int, input().split())) for i in range(n)]
a.sort(key=lambda x:x[0])
ans=0
c=0
for i in range(len(a)):
    c+=a[i][0]
    ans=ans+a[i][1]-c
print(ans)
