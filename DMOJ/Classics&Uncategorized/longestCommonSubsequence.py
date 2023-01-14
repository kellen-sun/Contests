import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, m = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

C = [[0 for i in range(1+n)] for j in range(1+m)]
for i in range(1,1+m):
    for j in range(1,1+n):
        if s2[i-1]==s1[j-1]:
            C[i][j] = C[i-1][j-1]+1
        else:
            C[i][j] = max(C[i][j-1], C[i-1][j])
print(C[m][n])