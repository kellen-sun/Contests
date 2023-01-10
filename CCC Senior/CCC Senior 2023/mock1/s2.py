import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

t = int(input())
for i in range(1,t):
    t*=i
    t%=998244353
print(t)