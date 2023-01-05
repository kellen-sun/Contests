#then convert dijkstra's from the node u want a pencil from and find the cheapest choice.
#add the pencil costs to all the destination city costs (removing the ones that don't sell)
import sys
input = sys.stdin.readline
INF = 10**12
n = int(input())
t = int(input())
graph = [[0 for j in range(n)] for i in range(n)]
for j in range(t):
    A,B,C = map(int, input().split())
    graph[A-1][B-1]=C
    graph[B-1][A-1]=C
k = int(input())
pencils = [list(map(int, input().split())) for i in range(k)]
pen = [-1 for i in range(n)]
for i in pencils:
    pen[i[0]-1]=i[1]
source = int(input())-1

dist = [float('inf') for i in range(len(graph))]
Q = [i for i in range(len(graph))]
dist[source] = 0
while Q:
    mm = [float("inf"),0]
    for i in Q:
        if dist[i]<mm[0]:
            mm = (dist[i], i)
    u=mm[1]
    Q.remove(u)
    for v in Q:
        if graph[u][v]!=0:
            alt = dist[u]+graph[u][v]
            if alt < dist[v]:
                dist[v]=alt

outout=INF
for i in range(n):
    if pen[i]!=-1:
        outout = min(dist[i]+pen[i], outout)
print(outout)