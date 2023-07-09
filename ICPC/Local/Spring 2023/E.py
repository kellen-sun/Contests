#sort by x values
#cuz have to visit all from west to east
import heapq
n = int(input())
volcanoes = [list(map(int, input().split())) for i in range(n)]

volcanoes.sort(key=lambda x: x[0])

distance = 0
distance += volcanoes[-1][0]-volcanoes[0][0]
#takes care of x position changes

#generate maxmin coordinates of each column
#generate graph
columns = set()
for i in volcanoes:
    if i[0] not in columns:
        columns.add(i[0])

#group volcanoes by columns
grouping = {}
for i in columns:
    grouping[i] = [10**7, -10**7]

for i in volcanoes:
    if i[1]>grouping[i[0]][1]:
        grouping[i[0]][1] = i[1]
    if i[1]<grouping[i[0]][0]:
        grouping[i[0]][0] = i[1]
print(grouping)
graph = [[] for i in range(1+2*len(grouping))]

graph[0].append((1, 0))
graph[0].append((2, 0))
KEYS = list(grouping.keys())
for i in range(len(grouping)-1):
    #going from __ and calculating top
    graph[2*i+1].append((2*i+3, abs(grouping[KEYS[i+1]][1]-grouping[KEYS[i]][0])))
    graph[2*i+1].append((2*i+4, abs(grouping[KEYS[i+1]][0]-grouping[KEYS[i]][0])))
    graph[2*i+2].append((2*i+3, abs(grouping[KEYS[i+1]][1]-grouping[KEYS[i]][1])))
    graph[2*i+2].append((2*i+4, abs(grouping[KEYS[i+1]][0]-grouping[KEYS[i]][1])))

dist = [(0,0)]
heapq.heapify(dist)
dd = [float('inf') for i in range(len(graph))]
dd[0] = 0
visited = [False for i in range(len(graph))]
while dist:
    u = heapq.heappop(dist)
    d = u[0]
    node = u[1]
    visited[node] = True
    for v in graph[node]:
        alt = dd[node]+v[1]
        if dd[v[0]]>alt and not visited[v[0]]:
            dd[v[0]]=alt
            heapq.heappush(dist, (alt, v[0]))

for i in grouping.keys():
    distance += grouping[i][1]-grouping[i][0]

print(distance+min(dd[-1], dd[-2]))