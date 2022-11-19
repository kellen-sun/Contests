n=int(input())
tides=list(map(int,input().split()))
t=sorted(tides)
first=t[:n//2]
second=t[n//2:]
ans=[]
for x in range(n//2):
    ans.append(first[n//2-1-x])
    ans.append(second[x])
print(*ans)
