import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for i in range(Q)]


zeros = [-1 for i in range(N)]
prev = -1
for i in range(len(arr)-1, -1, -1):
    if arr[i] == 0:
        prev = i
    zeros[i] = prev


ranges = []
lastseen = 0
for i in range(1, N):
    if arr[i-1] != arr[i]:
        ranges.append((lastseen, i-1))
        lastseen = i
ranges.append((lastseen, N-1))
def checker():
    global ranges, l, r
    if not ranges:
        return False
    a = 0
    b = len(ranges)-1
    c = (a+b)//2
    while a <= b:
        c = (a+b)//2
        if a==c:
            if l >= ranges[b][0] and l <= ranges[b][1]:
                c = b
                break
        if l >= ranges[c][0] and l <= ranges[c][1]:
            break
        if l >= ranges[c][0]:
            a,b = c, b
        else:
            a,b = a, c
    if r <= ranges[c][1]:
        return True
    return False


ds = [[] for i in range(2*10**6+30)]
ranges2 = []
C = 10**6 + 10
for i in range(N):
    val = arr[i]
    if ds[val + C]:
        ranges2.append((ds[val + C][-1], i))
    ds[-val + C].append(i)
ranges3 = sorted(ranges2)
#print(ranges3)
ds2 = [-1 for i in range(N+2)]
idx = len(ranges3)-1
for i in range(N-1, -1, -1):
    while True:
        if idx == -1:
            break
        if ranges3[idx][1]<=i:
            ds2[i] = ranges3[idx][0]
            break
        else:
            idx -= 1
#print(ds2)
def checker2(ranges2, ds2, l, r):
    #global ranges2, ds2, l, r
    # given the list of ranges
    # determine whether or not there's a range that fits in [l,r]
    # ranges2 sorted by 2nd element
    # find greatest range (i) in ranges2 st r_i <= r
    if not ranges2:
        return False
    a = 0
    b = len(ranges2)-1
    c = (a+b)//2
    while a<=b:
        c = (a+b)//2
        if a==c:
            if a!=b:
                #check b
                if ranges2[b][1]<=r:
                    c = b
                    break
            break
        if ranges2[c][1]<=r:
            a,b = c, b
        else:
            a,b = a,c
    x = ranges2[c][1]
    if ds2[x] >= l and x<=r:
        return True
    return False

for i in queries:
    can = False

    l, r = i[0]-1, i[1]-1
    if zeros[l] == -1:
        can = False
    elif zeros[l] > r:
        can = False
    else:
        can = True
    
    if not can:
        can = checker()

    if not can:
        can = checker2(ranges2, ds2, l, r)

    if can:
        print("YES")
    else:
        print("NO")
