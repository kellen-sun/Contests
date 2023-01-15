import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(m)]

graph = [[] for i in range(n)]
for i in edges:
    graph[i[0]-1].append((i[1]-1, i[2]))

dist = [(0,0)]
heapq.heapify(dist)
dd = [float('inf') for i in range(n)]
dd[0] = 0
visited = [False for i in range(n)]
while dist:
    u = heapq.heappop(dist)
    d = u[0]
    node = u[1]
    visited[node] = True
    for v in graph[node]:
        alt = dd[node]+v[1]
        if dd[v[0]]>alt and not visited[v[0]]:
            dd[v[0]]=alt
            #visited[v[0]]=True
            heapq.heappush(dist, (alt, v[0]))
print(*dd)
