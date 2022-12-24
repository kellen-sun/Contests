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

def search(start, graph):
    queue = deque([(start, [start], 0)])
    visited=[start]
    while queue:
        current = queue.popleft()
        node = current[0]
        paths = current[1]
        cost = current[2]
        for i in graph[node]:
            v=i[0]
            if len(paths)>1:
                if v!=paths[-2]:
                    p=paths.copy()
                    p.append(v)
                    if v==start:
                        if len(p)==len(set(p))+1:
                            return cost+i[1], p
                        else:
                            t=[]
                            for j in range(len(p)):
                                if p[j]==p[-1-j]:
                                    t.append(p[j])
                                else: break
                            return [False,t[:-1]]
                    queue.append((v, p, cost+i[1]))
                    visited.append(v)
            else:
                p=paths.copy()
                p.append(v)
                queue.append((v,p,cost+i[1]))
                visited.append(v)
    return [False,list(set(visited))]

sdist = dijkstra(s,graph)
edist = dijkstra(e,graph)

cyclecost = [-1 for i in range(n)]
for i in range(n):
    if cyclecost[i]==-1:
        ll=search(i, graph)
        if ll[0]!=False:
            for j in ll[1]:
                cyclecost[j]=ll[0]
        else:
            for j in ll[1]:
                cyclecost[j]=float('inf')
#print(cyclecost)
m = float('inf')
for i in range(n):
    alt=cyclecost[i]+sdist[i]+edist[i]
    if alt<m:
        m=alt
if m==float('inf'): m=-1
print(m)