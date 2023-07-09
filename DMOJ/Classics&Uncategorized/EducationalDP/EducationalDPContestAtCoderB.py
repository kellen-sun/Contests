import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

dp = [0 for i in range(n)]
for i in range(1, n):
    m = 10**10
    for j in range(max(i-k, 0), i):
        m = min(abs(array[i]-array[j]) + dp[j], m)
    dp[i] = m
print(dp[-1])