import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    arr=list(map(int, input().split()))
    graph[arr[0]].append((arr[1],arr[2]))
#find all path with the given start and end, then pick longest one

k=0
queue = deque([[[0],0]])
#the format of each element in queue is [current node, path until now]

while queue:
    current = queue.popleft()
    #print(current)
    queued = current[0]
    dist = current[1]
    node = queued[-1]
    if node == n-1:
        k=max(k, dist)
    else:
        for i in graph[node]:
            if i[0] not in queued:
                visited = queued.copy()
                visited.append(i[0])
                queue.append([visited, dist+i[1]])

print(k)