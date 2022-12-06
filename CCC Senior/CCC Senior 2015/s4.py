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
#print(graph)

dist = [[float('inf'),i] for i in range(n)]
Q = list(range(n))
dist[a] = [0,a]
heapq.heapify(dist)
dd = [float('inf') for i in range(n)]
dd[a] = 0
while dist:
    u = heapq.heappop(dist)
    d = u[0]
    node = u[1]
    print(node)
    #Q.remove(node) #this would be linear time though
    for v in graph[node]:
        alt = d+v[1]
        #print(v[0])
        if dd[v[0]]>alt:
            dd[v[0]]=alt
print(dd)