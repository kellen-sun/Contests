import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, w = map(int, input().split())
weights, values = zip(*[map(int, input().split()) for i in range(n)])
V = sum(values)+1
dp = [[float('inf') for j in range(V)] for i in range(n)]
for i in range(n):
    dp[i][0]=0
for i in range(n):
    for j in range(1, V):
        if i==0:
            if values[i]==j:
                dp[0][values[i]] = weights[i]
        else:
            if j>=values[i]:
                dp[i][j] = min(dp[i-1][j-values[i]]+weights[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
            
#print(dp)
for i in range(V):
    if dp[-1][V-1-i]<=w:
        print(V-1-i)
        break