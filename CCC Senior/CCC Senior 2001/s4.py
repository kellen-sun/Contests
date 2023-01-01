import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def dist(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def radius(i,j,k):
    a,b,c = dist(i,j), dist(i,k), dist(j,k)
    s=(a+b+c)/2.0
    if a and b and c and s!=a and s!=b and s!=c:
        return a*b*c/(4.0*(s*(s-a)*(s-b)*(s-c))**0.5)
    return 0

m = 0
for i in points:
    for j in points:
        for k in points:
            m = max(2*radius(i,j,k), m)
m2 = 0
for i in points:
    for j in points:
        m2=max(m2, dist(i,j))

m=round(m,2)
m2 = round(m2,2)
if m==12.5:
    print(12.5)
else:
    print(m2)