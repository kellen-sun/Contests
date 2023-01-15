
from itertools import combinations 
n=int(input())
apples=list(map(int, input().split()))
s=sum(apples)
comb=[]
for x in range(n+1):
    comb=comb+list(combinations(apples, x))
best=1000000000
for x in comb:
    if abs(s-sum(x)*2)<best:
        best=abs(s-sum(x)*2)
print(best)
