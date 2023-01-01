import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
pwd = [list(map(int, input().split())) for i in range(n)]
p,w,d = zip(*pwd)

def f(i,x):
    global p,w,d
    if x<p[i]-d[i]: return w[i]*(p[i]-d[i]-x)
    if x>p[i]+d[i]: return w[i]*(x-p[i]-d[i])
    return 0

def F(x):
    global n
    return sum([f(i,x) for i in range(n)])

low = min(p)
high = max(p)

def binary_search(low, high):
    current = (low+high)//2
    val = F(current)
    vnext = F(current+1)
    vprev = F(current-1)
    #print(current)
    if vprev>val and val<=vnext:
        return current
    if vprev>val and val>vnext:
        return binary_search(current, high)
    return binary_search(low, current)

print(F(binary_search(low, high)))
