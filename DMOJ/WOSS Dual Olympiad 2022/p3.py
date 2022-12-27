import sys
import heapq
from collections import deque
input = sys.stdin.readline

n,m=map(int, input().split())
roads = [tuple(map(int, input().split())) for i in range(m)]
s,e = map(int, input().split())
s,e=s-1, e-1

#bfs to find distance of S and E to all nodes (dijkstra)
#find all cycles and find their cost
#loop through all nodes that are in a cycle
#find the one that minimizes -> cyclecost+dist(s,node)+dist(e,node)
#cyclecost is an array, each index (node number) corresponds to the cost of its cycle, -1 if not in a cycle

graph = [[] for i in range(n)]
for i in roads:
    graph[i[0]-1].append((i[1]-1,i[2]))
    graph[i[1]-1].append((i[0]-1,i[2]))

def dijkstra(start, graph):
    global n
    queue = [(0, start)]
    dist = [float('inf') for i in range(n)]
    dist[start]=0
    heapq.heapify(queue)
    while queue:
        u = heapq.heappop(queue)
        node = u[1]
        for v in graph[node]:
            alt = dist[node]+v[1]
            if alt<dist[v[0]]:
                dist[v[0]]=alt
                heapq.heappush(queue, (alt, v[0]))
    return dist

def dfs_cycle(u,t,p):
    global cycles, parent, vis_num, graph
    if vis_num[u]==2:
        return
    if vis_num[u]==1:
        cycles.append([[u], t])
        curr=p
        while curr!=u:
            cycles[-1][0].append(curr)
            cycles[-1][1]+=parent[curr][1]
            curr=parent[curr][0]
        return
    parent[u] = [p,t]
    vis_num[u]=1
    for node in graph[u]:
        if node[0]!=parent[u][0]:
            dfs_cycle(node[0],node[1],u)
    vis_num[u]=2


sdist = dijkstra(s,graph)
edist = dijkstra(e,graph)

cycles=[]
parent = [[0,0] for i in range(200005)]
vis_num = [0 for i in range(200005)]
for i in range(n):
    if vis_num[i]==0:
        dfs_cycle(i,0,-1)
#dfs_cycle(1, 0, -1)

cyclecost = [float('inf') for i in range(n)]
for i in cycles:
    cost = i[1]
    for j in i[0]:
        cyclecost[j]=cost

m = float('inf')

for i in range(n):
    alt=cyclecost[i]+sdist[i]+edist[i]
    if alt<m:
        m=alt
if m==float('inf'): m=-1
print(m)