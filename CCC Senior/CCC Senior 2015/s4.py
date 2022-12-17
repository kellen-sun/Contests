import sys
import heapq
input = sys.stdin.readline

k,n,m = map(int, input().split())

graph = [{} for i in range(n)]
for i in range(m):
    a,b,t,h = map(int, input().split())
    graph[a-1].setdefault(b-1,[]).append((t,h))
    graph[b-1].setdefault(a-1,[]).append((t,h))
a,b = map(int, input().split())
a-=1
b-=1

dist = [(0,a,k)]
heapq.heapify(dist)
INF = 10**10
dd = [[INF for i in range(201)] for j in range(n)]
dd[a][k] = 0
min_time=INF
visited=set()
while dist:
    u = heapq.heappop(dist)
    if u[1]==b:
        min_time=u[0]
        break
    if u[1:] in visited:
        continue
    visited.add(u[1:])
    node=u[1]
    for v in graph[node]:
        for route in graph[node][v]:
            alt = (dd[node][u[2]]+route[0], v, u[2]-route[1])
            if alt[2]>0:
                if alt[0]<dd[alt[1]][alt[2]]:
                    dd[alt[1]][alt[2]]=alt[0]
                heapq.heappush(dist, alt)
min_time = min(dd[b])
if min_time==INF:
    min_time=-1
print(min_time)