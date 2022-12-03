m,n = map(int, input().split())
roads = [tuple(map(lambda x : x[0], input().split())) for i in range(m)]
queries = [tuple(map(lambda x : x[0], input().split())) for i in range(n)]
#run a bfs on each query put the ouputs into out print out
graph = {}
for i in roads:
    if graph.get(i[0])!=None:
        graph[i[0]].append(i[1])
    else:
        graph[i[0]]=[i[1]]
    if graph.get(i[1])!=None:
        graph[i[1]].append(i[0])
    else:
        graph[i[1]]=[i[0]]
#print(graph)
out = []
def bfs(graph, start, end):
    #will need to trackpath on this bfs
    queue = [start]
    queued = {}
    path = {}
    for i in graph.keys():
        queued[i]=False
        path[i]=[]
    path[start].append(start)
    while queue:
        current = queue.pop(0)
        if current == end:
            return "".join(path[end])
        for i in graph[current]:
            if not queued[i]:
                queued[i]=True
                queue.append(i)
                path[i]=path[current]+[i]
for i in queries:
    out.append(bfs(graph, i[0], i[1]))
for i in out:
    print(i)