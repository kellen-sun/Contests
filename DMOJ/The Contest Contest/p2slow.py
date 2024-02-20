import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))
counts = [[] for i in range(k)]
for i in range(n):
    if arr[i]-1<k:
        counts[arr[i]-1].append(i)


for i in range(k):
    prev = queries[i]+1
    new = arr[:]
    j = 0
    while True:
        if j==len(new):
            break
        if new[j] == i+1:
            k = 0
            while True:
                new.pop(j)
                j-=1
                k+=1
                if k==prev or j==-1:
                    break
        j+=1
    #print(new)
    print(sum(new))
