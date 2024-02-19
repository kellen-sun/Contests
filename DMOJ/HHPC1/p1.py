import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

t = int(input())
output = []

def f():
    n = int(input())
    s = input()
    ranges = []
    m = 0
    lastseen = 0
    for i in range(1, n):
        if s[i-1] != s[i]:
            ranges.append((lastseen, i-1, s[i-1]))
            lastseen = i
    ranges.append((lastseen, n-1, s[n-1]))
    #print(ranges)
    m = max(ranges, key=lambda x: x[1]-x[0])
    m = m[1]-m[0]
    if len(ranges) != 1:
        m += 1
    for i in range(2, len(ranges)):
        if ranges[i][2] == ranges[i-2][2]:
            if ranges[i][0] - 2 == ranges[i-2][1]:
                m = max(ranges[i][1] - ranges[i-2][0], m)
    return m+1

for _ in range(t):
    output.append(f())
for i in output:
    print(i)