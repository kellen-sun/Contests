import sys
import heapq
from collections import deque
input = sys.stdin.readline

n,m=map(int, input().split())
roads = [tuple(map(int, input().split())) for i in range(m)]
s,e = map(int, input().split())
s,e=s-1, e-1

#bfs to find distance of S and E to all nodes
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

def dfs_cycle(node, parent, color, par, cost):
    global cyclenumber
    if color[node]==2:
        return
    if color[node]==1:
        v=[]
        cyclecost=0
        cur=parent
        v.append(cur)
        #print(par, node)
        while cur!=node:
            cyclecost+=par[cur][1]
            #print("node", par[cur][0],"weight",par[cur][1])
            cur=par[cur][0]
            
            v.append(cur)
        start=v[0]
        end=v[-1]
        for i in graph[start]:
            if i[0]==end:
                cyclecost+=i[1]
                break
        
        cycles[cyclenumber]=(v,cyclecost)
        cyclenumber+=1
        return
    if parent!=-1:
        par[node]=(parent, cost)
        color[node]=1
    for vv in graph[node]:
        v=vv[0]
        if v==parent:
            continue
        dfs_cycle(v, node, color, par, vv[1])
    color[node]=2

sdist = dijkstra(s,graph)
edist = dijkstra(e,graph)

cycles=[[] for i in range(n)]
cyclenumber=0
dfs_cycle(1, -1, [0]*n, [0]*n, 0)
#print(cycles)
cyclecost = [float('inf') for i in range(n)]
for i in range(cyclenumber):
    cost = cycles[i][1]
    for j in cycles[i][0]:
        cyclecost[j]=cost

m = float('inf')

for i in range(n):
    alt=cyclecost[i]+sdist[i]+edist[i]
    if alt<m:
        m=alt
if m==float('inf'): m=-1
print(m)