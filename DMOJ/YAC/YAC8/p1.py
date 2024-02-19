import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tot = n
m = 0
for i in range(n):
    if arr[i] == i+1:
        if m < i+1:
            tot -= 1
    if arr[i] > m:
        m = arr[i]
print(tot)