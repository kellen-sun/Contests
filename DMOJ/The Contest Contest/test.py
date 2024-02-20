import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline
import random

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
            i -= 1
        else:
            push -= intervals[i][0] - intervals[i-1][1]-1
            l,r = intervals.pop(i)
            i -= 1
            intervals[i][1] = r

def f1(n,k,arr, queries):   
    out = []       
    counts = [[] for i in range(k)]
    for i in range(n):
        if arr[i]-1<k:
            counts[arr[i]-1].append(i)
    psa = [0]
    for i in arr:
        psa.append(psa[-1]+i)

    for i in range(k):
        prev = queries[i]
        intervals = []
        for j in counts[i]:
            left = j-prev
            intervals.append([left, j])
        # print(intervals)
        intervals = transform(intervals)
        s = 0
        # print(intervals)
        for j in intervals:
            s += psa[j[1]+1] - psa[j[0]]
        out.append(psa[-1] - s)
    return out

def f2(n,k,arr, queries):
    out = []
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
        out.append(sum(new))
    return out


while True:
    n = random.randint(2,8)
    k = random.randint(2,n)
    arr = [random.randint(1, k) for i in range(n)]
    queries = [random.randint(1,n) for i in range(k)]
    if f1(n,k,arr,queries)!=f2(n,k,arr,queries):
        print(n)
        print(k)
        print(*arr)
        print(*queries)
        break