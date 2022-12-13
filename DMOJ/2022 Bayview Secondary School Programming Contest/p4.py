import sys
from collections import deque
input = sys.stdin.readline

n,t = map(int, input().split())
times = list(map(int, input().split()))
cc=0
for i in range(n):
    cc+=times[i]
    if cc>t:
        break

t+=max(times[:i+1])
cc=0
broke = False
for i in range(n):
    cc+=times[i]
    if cc>t:
        print(i-1)
        broke = True
        break
if not broke: print(i)