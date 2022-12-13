import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    a=int(input())
    if a==0:
        array.pop(-1)
    else:
        array.append(a)
print(sum(array))