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
psa = [0]
for i in arr:
    psa.append(psa[-1]+i)

# print(psa)
# print(counts)

def transform(intervals):
    if not intervals:
        return intervals
    i = len(intervals)-1
    push = 0
    while True:
        if i==0:
            intervals[i][0] = max(0, intervals[i][0]-push)
            return intervals
        if intervals[i][0] > intervals[i-1][1]+1+push:
            intervals[i][0] = intervals[i][0]-push
            push = 0
            i -= 1
        else:
            push -= intervals[i][0] - intervals[i-1][1]-1
            l,r = intervals.pop(i)
            i -= 1
            intervals[i][1] = r
            


for i in range(k):
    prev = queries[i]
    intervals = []
    for j in counts[i]:
        left = j-prev
        intervals.append([left, j])
    #print(intervals)
    intervals = transform(intervals)
    s = 0
    #print(intervals)
    for j in intervals:
        s += psa[j[1]+1] - psa[j[0]]
    print(psa[-1] - s)

#print(transform([[3,5], [4,6]]))

