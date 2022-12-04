
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
grid = [input()[:-1] for i in range(n)]

def init_queued(a):
    global n
    global m
    queued = {}
    for i in range(n):
        for j in range(m):
            queued[(i,j)]=a
    return queued
graph = [[] for i in range(n*m)]
for i in range(n):
    for j in range(m):
        if grid[i][j]=="N":
            graph[i*n+j].append(i*n-n+j)
            graph[i*n-n+j].append(i*n+j)
        elif grid[i][j]=="S":
            graph[i*n+j].append(i*n+j+n)
            graph[i*n+j+n].append(i*n+j)
        elif grid[i][j]=="W":
            graph[i*n+j].append(i*n+j-1)
            graph[i*n+j-1].append(i*n+j)
        elif grid[i][j]=="E":
            graph[i*n+j].append(i*n+j+1)
            graph[i*n+j+1].append(i*n+j)
in_component = [False for i in range(n*m)]
components = 0
#print(graph)
for i in range(n):
    for j in range(m):
        if not in_component[i*n+j]:
            components+=1
            queue = deque([i*n+j])
            in_component[i*n+j]=True
            while queue:
                current = queue.popleft()
                #print(current)
                for kk in graph[current]:
                    if not in_component[kk]:
                        queue.append(kk)
                        in_component[kk]=True

print(components)