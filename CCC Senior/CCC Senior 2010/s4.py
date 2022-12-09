import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
pens = [list(map(int, input().split())) for i in range(n)]
edges = {} #edges and which vertices they connect at what weight
edges2 = [] #what pens do those edges connect
for i in range(n):
    for j in range(pens[i][0]):
        v1=pens[i][j+1]
        v2=pens[i][(j+1)%pens[i][0]+1]
        edge = (min(v1,v2), max(v1,v2))
        w = pens[i][j+pens[i][0]+1]
        if edges.get(edge)==None:
            edges[edge]=(i,w)
        else:
            edges2.append((edges[edge][0],i,w))
            edges.pop(edge)

for i in edges.keys():
    edges2.append((n,edges[i][0],edges[i][1]))
min_edges = {}
for i in edges2:
    if  min_edges.get((i[0],i[1]))==None:
        min_edges[(i[0],i[1])]=i[2]
    else:
        min_edges[(i[0],i[1])]=min(i[2],min_edges[(i[0],i[1])])
min_edges2 = []
for i in min_edges.keys():
    min_edges2.append((i[0],i[1],min_edges[i]))
sorted_edges = sorted(min_edges2, key=lambda x:x[2])
#print(sorted_edges)


def find(x, link):
    while x!=link[x]:
        x=link[x]
    return x

def same(a,b,link):
    return find(a,link)==find(b,link)

def unite(a,b,size,link):
    a=find(a, link)
    b=find(b,link)
    if size[a]<size[b]:
        c=a
        a=b
        b=c
    size[a]+=size[b]
    link[b]=a
    return size, link

def kruskal(edges, n):
    link = [i for i in range(n)]
    size = [1 for i in range(n)]
    weight = 0
    for i in edges:
        a,b = i[0],i[1]
        if not a == n:
            if not same(a,b,link):
                weight += i[2]
                size,link = unite(a,b, size, link)

    return weight
print(min(kruskal(sorted_edges, n), kruskal(sorted_edges,n+1)))
