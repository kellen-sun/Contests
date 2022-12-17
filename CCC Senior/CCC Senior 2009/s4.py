#then convert dijkstra's from the node u want a pencil from and find the cheapest choice.
#add the pencil costs to all the destination city costs (removing the ones that don't sell)
import sys
import heapq
input = sys.stdin.readline

n = int(input())
t = int(input())
#adjacency matrix uses too much memory
graph = [[] for i in range(n)]
for i in range(t):
    a,b,c=map(int, input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

k = int(input())
pencils = [list(map(int, input().split())) for i in range(k)]
pen = [-1 for i in range(n)]
for i in pencils:
    pen[i[0]-1]=i[1]
source = int(input())-1

dist = [(0,source)]
heapq.heapify(dist)
dd = [float('inf') for j in range(n)]
dd[source] = 0
while dist:
    u = heapq.heappop(dist)
    d = u[0]
    node = u[1]
    for v in graph[node]:
        alt = d+v[1]
        if dd[v[0]]>alt:
            dd[v[0]]=alt
            heapq.heappush(dist, (alt, v[0]))

outout=float('inf')
for i in range(n):
    if pen[i]!=-1:
        outout = min(dd[i]+pen[i], outout)
print(outout)
#faster way??