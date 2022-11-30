#then convert dijkstra's from the node u want a pencil from and find the cheapest choice.
#add the pencil costs to all the destination city costs (removing the ones that don't sell)
import sys
input = sys.stdin.readline
n = int(input())
t = int(input())
roads = [list(map(int, input().split())) for i in range(t)]
k = int(input())
pencils = [list(map(int, input().split())) for i in range(k)]
pen = [-1 for i in range(n)]
for i in pencils:
    pen[i[0]-1]=i[1]

d = int(input())

graph = [[0 for j in range(n)] for i in range(n)]
for i in roads:
    graph[i[0]-1][i[1]-1]=i[2]
    graph[i[1]-1][i[0]-1]=i[2]

def dijkstra(graph, source):
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
    return dist
out = dijkstra(graph, d-1)

outout=[]
for i in range(len(out)):
    if pen[i]!=-1:
        outout.append(out[i]+pen[i])
print(min(outout))