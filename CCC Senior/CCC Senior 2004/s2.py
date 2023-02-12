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
