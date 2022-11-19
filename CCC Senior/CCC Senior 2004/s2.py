a=input().split()
n=int(a[0])
k=int(a[1])

rank=[]
points=[0 for i in range(n)]
for x in range(k):
    current=list(map(int, input().split()))
    for y in range(len(current)):
        points[y]+=current[y]
    rank.append(points)
ind=rank[-1].index(max(rank[-1]))
print(ind+1)
print(rank[-1][ind])
ranks=[]
for x in rank:
    y=x[ind]
    x.sort()
    ranks.append(x.index(y))

print(min(ranks)+1)
