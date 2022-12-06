n,m=map(int, input().split())
pho = list(map(int, input().split()))
graph=[[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
queue = []

for i in range(n):
    if len(graph[i]) == 1:
        queue.append(i)
visited = [False for i in range(n)]
while queue:
    current = queue.pop(0)
    if current not in pho and not visited[current] and len(graph[current])==1:
        parent = graph[current][0]
        queue.append(parent)
        graph[current]=[]
        graph[parent].remove(current)
        visited[current]=True
for i in range(n):
    if graph[i]!=[]:
        start = i
        break
queue = [start]
dist = [0 for i in range(n)]
queued = [False for i in range(n)]
queued[start]=True
while queue:
    current = queue.pop(0)
    for i in graph[current]:
        if not queued[i]:
            dist[i]=dist[current]+1
            queue.append(i)
            queued[i]=True
start = -1
m = -1
for i in range(len(dist)):
    if dist[i]>m:
        m=dist[i]
        start = i

queue = [start]
dist = [0 for i in range(n)]
queued = [False for i in range(n)]
queued[start]=True
while queue:
    current = queue.pop(0)
    for i in graph[current]:
        if not queued[i]:
            dist[i]=dist[current]+1
            queue.append(i)
            queued[i]=True
mmm=0
for i in graph:
    if i!=[]: mmm+=1
print(2*mmm-2-max(dist))