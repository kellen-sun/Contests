import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
left = [i for i in range(1, g+1)]
count = 0
for i in planes:
    curmaxindex = False
    #print(left)
    for j in range(len(left)):
        if left[j]<=i:
            curmaxindex = j
        else:
            break
    if isinstance(curmaxindex, bool):
        break
    else:
        count+=1
        left.pop(curmaxindex)
print(count)