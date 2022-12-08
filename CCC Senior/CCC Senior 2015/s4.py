import sys
import heapq
from collections import deque
input = sys.stdin.readline

k,n,m = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(m)]
a,b = map(int, input().split())
a-=1
b-=1

graph = [[] for i in range(n)]
for i in edges:
    graph[i[0]-1].append((i[1]-1, i[2], i[3]))
    graph[i[1]-1].append((i[0]-1, i[2], i[3]))

dist = [(0,a,0)]
heapq.heapify(dist)
dd = [[float('inf') for i in range(k)] for j in range(n)]
dd[a][0] = 0
visited = [[False for i in range(k)] for j in range(n)]
while dist:
    u = heapq.heappop(dist)
    d = u[0]
    node = u[1]
    damage = u[2]
    visited[node][damage] = True
    for v in graph[node]:
        #print(v)
        for add_dmg in range(k-v[2]):
            alt = dd[node][add_dmg]+v[1]
            if dd[v[0]][add_dmg+v[2]]>alt and not visited[v[0]][add_dmg+v[2]]:
                dd[v[0]][add_dmg+v[2]]=alt
                heapq.heappush(dist, (alt, v[0], add_dmg+v[2]))
a = min(dd[b])
if a==float("inf"):
    print(-1)
else:
    print(a)