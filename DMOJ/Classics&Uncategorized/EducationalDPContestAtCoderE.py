import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, w = map(int, input().split())
items = [0]
for i in range(n): items.append(list(map(int, input().split())))

dp = [0 for i in range(w+1)]
dp1 = [0 for i in range(w+1)]
for i in range(1, n+1):
    value = items[i-1][1]
    weight = items[i-1][0]
    for j in range(w+1):
        if j<weight:
            dp1[j] = dp[j]
        else:
            dp1[j] = max(dp[j], dp[j-weight]+value)
    dp = dp1[:]
print(dp1[-1])