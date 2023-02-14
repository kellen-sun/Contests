n=int(input())
tides=list(map(int,input().split()))
t=sorted(tides)
first=t[:(n+1)//2]
second=t[(n+1)//2:]
ans=[]
for x in range(n):
    if x%2==0:
        ans.append(first.pop(-1))
    else:
        ans.append(second.pop(0))
print(*ans)
