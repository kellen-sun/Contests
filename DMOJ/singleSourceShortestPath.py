import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]
graph = [[float("inf") for j in range(n)] for i in range(n)]
for i in edges:
    if graph[i[0]-1][i[1]-1] > i[2]:
        graph[i[0]-1][i[1]-1]=i[2]
        graph[i[1]-1][i[0]-1]=i[2]
def dijkstra(graph, source):
    dist = [float('inf') for i in range(len(graph))]
    Q = [i for i in range(len(graph))]
    dist[source] = 0
    while Q:
        mm = [float("inf"), 0]
        for i in Q:
            if dist[i]<=mm[0]:
                mm = (dist[i], i)
        u=mm[1]
        Q.remove(u)
        for v in Q:
            if graph[u][v]!=0:
                alt = dist[u]+graph[u][v]
                if alt < dist[v]:
                    dist[v]=alt
    return dist
dist = dijkstra(graph, 0)
for i in dist:
    if i==float("inf"):
        print(-1)
    else:
        print(i)