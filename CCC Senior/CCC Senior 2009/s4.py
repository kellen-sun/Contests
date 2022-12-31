#dijkstra's from the node u want a pencil from and find the cheapest choice.
#add the pencil costs to all the destination city costs (removing the ones that don't sell)
import sys
import heapq
input = sys.stdin.readline
INF = 10**12

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

dd = [INF for j in range(n)]
dd[source] = 0
visited = set()
while len(visited)!=n:
    currentmin = INF
    for i in range(len(dd)):
        if dd[i]<currentmin and (i not in visited):
            currentmin=dd[i]
            currentminindex = i
    d = currentmin
    node = currentminindex
    if node in visited:
        continue
    visited.add(node)
    for v in graph[node]:
        alt = d+v[1]
        if dd[v[0]]>alt:
            dd[v[0]]=alt

outout=INF
for i in range(n):
    if pen[i]!=-1:
        outout = min(dd[i]+pen[i], outout)
print(outout)