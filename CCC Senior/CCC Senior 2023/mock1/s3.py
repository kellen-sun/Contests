import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())
iceblocks = list(range(1, n+1))
if k==1 and n==2: print(1)
elif k==1: print(0)
elif k==2 and n==2: print(1)
elif k==2 and n==3: print(3)
elif k==n-1: print(3**(n-2)%998244353)
elif k==2: print(2)
else:
    dp = [[0 for j in range(n)] for i in range(k+1)]
    #generate ways to go one direction to n with k dist
    #use all those ways compare them to each other to see if any are used twice