import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

m = 0
for i in range(n//2):
    m = max(m, i*(n-i*2)*(n-i*2-1)//2)
print(m)