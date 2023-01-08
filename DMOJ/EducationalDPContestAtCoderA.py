import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
if n>2:
    dp = [0 for i in range(n)]
    dp[1] = abs(array[1]-array[0])
    dp[2] = abs(array[2]-array[0])
    for i in range(3,n):
        dp[i]=min(abs(array[i]-array[i-1])+dp[i-1], abs(array[i]-array[i-2])+dp[i-2])
    print(dp[-1])
else:
    print(abs(array[0]-array[1]))