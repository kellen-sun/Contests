import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
happy = [list(map(int, input().split())) for i in range(n)]

dp = [[0,0,0] for i in range(n)]
dp[0] = happy[0]
for i in range(1,n):
    dp[i][0] = happy[i][0]+max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = happy[i][1]+max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = happy[i][2]+max(dp[i-1][1], dp[i-1][0])

print(max(dp[-1]))