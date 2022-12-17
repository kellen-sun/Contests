import sys
import heapq
from collections import deque
input = sys.stdin.readline

n,w,d = map(int, input().split())
walkways = [tuple(map(int, input().split())) for i in range(w)]
train = list(map(int, input().split()))
days = [tuple(map(int, input().split())) for i in range(d)]

graph = [[] for i in range(n)]
for i in walkways:
    graph[i[1]-1].append((i[0]-1,1))
#actually want the distance from each station to end using only walkways can be done with bfs
queue = deque([n-1])
dist = [float('inf') for i in range(n)]
dist[n-1]=0
while queue:
    current = queue.popleft()
    for i in graph[current]:
        if dist[i[0]]>dist[current]+1:
            dist[i[0]]=dist[current]+1
print(dist)
#O(N+W) to run the bfs

#for a specific train path, minimize S_0 to S_i time + S_i to S_n
#a simple loop for each day would be O(D*N)

for i in range(d):
    temp = train[days[i][0]-1]
    train[days[i][0]-1]=train[days[i][1]-1]
    train[days[i][1]-1]=temp
    m=float('inf')
    for j in range(n):
        m=min(j+dist[train[j]-1],m)
    print(m)
