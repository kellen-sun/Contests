import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
hall = [input(), input()]
count = 0
for i in range(n):
    if hall[0][i]=="S" and hall[1][i]=="S":
        count+=1
if count>2:
    print("NO")
else: 
    print("YES")