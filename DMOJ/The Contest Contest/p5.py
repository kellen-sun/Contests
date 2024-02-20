import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

m,k = map(int, input().split())
ov = [map(int, input().split()) for i in range(k)]
MOD = 10**9 + 7
if k==0:
    print((m+m//2+(m%2)*2))
    if m%2:
        print((pow(2, (m//2), MOD) * (m//2 + 1))%MOD)
    else:
        print(pow(2, (m//2), MOD))
else:
    print((m//2 + 1))
    if m%2:
        print((m//2 + 1)%MOD)
    else:
        print(1)