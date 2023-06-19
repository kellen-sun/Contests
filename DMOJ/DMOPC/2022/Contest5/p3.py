import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
b = [array[0]]
for i in array[1:]:
    b.append(i^b[-1])
print(b)
