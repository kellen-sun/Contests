import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
a=[]
b=[]
for i in range(n):
    kk = list(map(int, input().split()))
    a.append(kk[0])
    b.append(kk[1])
if n==m:
    c=0
    a=sorted(a, reverse=True)
    for i in range(n):
        c+=i*a[i]
    c+=sum(b)
    print(c)