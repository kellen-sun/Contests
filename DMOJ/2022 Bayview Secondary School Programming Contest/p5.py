import sys
from collections import deque
input = sys.stdin.readline

mod = int(1e9+7)
n=int(input())
heights = list(map(int, input().split()))
def deg(n):
    if n%2==0:
        return 1+deg(n//2)
    else:
        return 0
c=1
for i in heights:
    k=deg(i)
    if k!=0:
        kk=(3*(2**(k-1))-1)
        c=c*kk%mod
print(c%mod)