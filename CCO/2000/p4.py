from collections import deque
n,w,p = map(int, input().split())
wires = [tuple(map(int, input().split())) for i in range(w)]
packets = [tuple(map(int, input().split())) for i in range(p)]

graph=[[] for i in range(n)]
for i in wires:
    graph[i[0]-1].append((i[1]-1, i[2]))
    graph[i[1]-1].append((i[0]-1, i[2]))

out = []
dist = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    queue = deque([i])
    queued = [False for i in range(n)]
    while queue:
        current = queue.popleft()
        for j in graph[current]:
            if not queued[j[0]]:
                queued[j[0]] = True
                queue.append(j[0])
                dist[i][j[0]]=dist[i][current]+j[1]

for i in packets:
    print(dist[i[0]-1][i[1]-1])