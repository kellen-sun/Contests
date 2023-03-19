import math
n = int(input())
array = list(map(int, input().split()))
queued = []
queue = [array]
while queue:
    cur = queue.pop(0)
    for i in range(n-2):
        if math.gcd(cur[i], cur[i+1])==1:
            a=cur.copy()
            a[i]=cur[i+1]
            a[i+1]=cur[i]
            if a not in queued:
                queued.append(a)
                queue.append(a)
m=0
mmm=[]
for i in queued:
    mm=""
    for j in i:
        mm+=str(j)
    mm=int(mm)
    if mm>m:
        m=mm
        mmm=i
print(*mmm)