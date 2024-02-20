import sys
import itertools
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

if n<=7:
    done = False
    ALL = list(itertools.product(list(range(1,n+1)), repeat=n))
    for arr in ALL:
        v = 0
        for i in range(n):
            if a[i] != sum([1 if arr[j]<arr[i] else 0 for j in range(i)]):
                v += 1
                if v>1:
                    break
            if b[i] != sum([1 if arr[j]<arr[i] else 0 for j in range(i+1, n)]):
                v += 1
                if v>1:
                    break
            if c[i] != sum([1 if arr[j]>arr[i] else 0 for j in range(i)]):
                v += 1
                if v>1:
                    break
            if d[i] != sum([1 if arr[j]>arr[i] else 0 for j in range(i+1, n)]):
                v += 1
                if v>1:
                    break
        if v < 2:
            print(*arr)
            done = True
            break
    if not done:
        print(-1)
else:
    # case 2 is monotone (but not strict)
    v = 0
    for i in range(n):
        a[i]+d[i] == n-1