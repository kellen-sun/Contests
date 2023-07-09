import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, w = map(int, input().split())
items = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for i in range(w+1)] for j in range(n+1)]

for i in range(1, n+1):
    value = items[i-1][1]
    weight = items[i-1][0]
    for j in range(w+1):
        if j<weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[-1][-1])