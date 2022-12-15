import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
edges = int(input())
graph = [[] for i in range(n+m)]
for i in range(edges):
    a,b = map(int, input().split())
    graph[a-1].append(n+b-1)
    graph[n+b-1].append(a-1)

out = "YES"
for i in range(n):
    a=set(graph[i])
    for j in range(n):
        if i!=j:
            b=set(graph[j])
            if len(a.intersection(b))>1:
                out = "NO"
    if out=="NO":
        break
print(out)
