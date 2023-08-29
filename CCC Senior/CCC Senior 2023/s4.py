import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

all_edges = []
for i in range(m):
    a,b,l,c = map(int, input().split())
    all_edges.append((a-1, b-1, l, c))
    all_edges.append((b-1, a-1, l, c))
link = [i for i in range(n)]
size = [1 for i in range(n)]
totalc = 0
graph = [[] for i in range(n)]

def dijkstra(a,b,graph):
    dist = [0 for i in range(n)]
    Q=[]
    heapq.heapify(Q)
    for i in range(n):
        if i!=a:
            dist[i] = float('inf')
    heapq.heappush(Q, (dist[a], a))
    while Q:
        u = heapq.heappop(Q)
        for v in graph[u[1]]:
            alt = dist[u[1]]+v[1]
            if alt<dist[v[0]]:
                dist[v[0]] = alt
                heapq.heappush(Q, (alt, v[0]))
    return dist[b]

all_edges.sort(key = lambda x:(x[2], x[3]))
for i in all_edges:
    a,b = i[0], i[1]
    if dijkstra(a,b,graph)>i[2]:
        totalc+=i[3]
        graph[a].append((b, i[2]))
        graph[b].append((a, i[2]))
print(totalc)
