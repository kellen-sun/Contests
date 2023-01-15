import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

s1 = input()[:-1]
s2 = input()[:-1]

n,m = len(s1), len(s2)
C = [[0 for i in range(n)] for j in range(m)]
for i in range(1,m):
    for j in range(1,n):
        if s2[i-1]==s1[j-1]:
            C[i][j] = C[i-1][j-1]+1
        else:
            C[i][j] = max(C[i][j-1], C[i-1][j])
#print(C)
i = m-1
j = n-1
out = ""
while i>0 and j>0:
    if s2[i]==s1[j]:
        out=s2[i]+out
        i-=1
        j-=1
    if C[i][j]==C[i-1][j]:
        i-=1
    if C[i][j]==C[i][j-1]:
        j-=1
if s1[0]==s2[0]:
    out = s1[0]+out
print(out)