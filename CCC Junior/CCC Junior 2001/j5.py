roads=[]
while True:
    a=input('')
    if a=="**":
        break
    roads.append(a)

def bfs(graph, end, path, queued, start):
    queue=[[start]]
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node == end:
            return 'possible'
        elif node not in queued:
            for current_neighbour in graph.get(node, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
            queued.append(node)
    return 'impossible'
            
            
def make_graph(roads):
    graph={}
    for x in range(len(roads)):
        if roads[x][0] not in graph.keys():
            graph[roads[x][0]]=[roads[x][1]]
        else:
            graph[roads[x][0]].append(roads[x][1])
        if roads[x][1] not in graph.keys():
            graph[roads[x][1]]=[roads[x][0]]
        else:
            graph[roads[x][1]].append(roads[x][0])
    return bfs(graph, 'B', ['A'], [], 'A')
    
bomb_roads=[]
for x in range(len(roads)):
    road=roads.pop(x)
    if make_graph(roads)=='impossible':
        bomb_roads.append(road)
    roads.append(road)

bomb_roads = list(dict.fromkeys(bomb_roads))
for x in range(len(bomb_roads)):
    print(bomb_roads[x])
print('There are '+str(len(bomb_roads))+' disconnecting roads.')
