import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(input())

l = 0
for i in range(len(arr)):
    if arr[i]=="Y":
        l = i
l+=1
if l>n/2:
    print("YES")
else:
    print("NO")