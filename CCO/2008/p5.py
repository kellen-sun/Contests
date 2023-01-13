import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
coins = []
for i in range(n):
    k,c = map(int, input().split())
    for j in range(k): coins.append(c)

total = sum(coins)
half = total//2

dp = [False for i in range(total+1)]
dp[0] = True
for k in range(len(coins)):
    for x in range(total,-1,-1):
        if dp[x]:
            dp[x+coins[k]]=True

closest = 0
for i in range(len(dp)):
    if dp[i] and abs(half-i)<abs(half-closest):
        closest = i
print(abs(total-2*closest))