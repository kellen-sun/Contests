import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def run():
    n,k,a,b,c = map(int, input().split())
    if b==0 and c==0:
        mx = (n-k)*a + a*((k-1)//2)
        mn = 0
        return [mx, mn]
    if b==0:
        #this assumes a>c
        if a>c:
            mx = (n-k)*a + a*((k-1)//2) + c*(k-1 - (k-1)//2)
        else:
            mx = (n-k)*c + c*((k-1)//2) + a*(k-1 - (k-1)//2)
        mn = 0
        return [mx, mn]
    if c==0:
        mx = max((n-k)*a + a*((k-1)//2), (n-k)*a + b*(k-1))
        mn = min(b*(n-k), a*(n-k - (n-k)//2))
        return [mx, mn]
    else:
        if c>a:
            a,c = c,a
        
    return [0,0]

T = int(input())
for i in range(T):
    print(*run())