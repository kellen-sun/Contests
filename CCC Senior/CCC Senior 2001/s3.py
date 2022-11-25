roads = []
while True:
    i = input()
    if i=="**":
        break
    roads.append(i)
output = []
for j in roads:
    graph = {}
    for i in roads:
        if i==j:
            continue
        if i[0] not in graph.keys():
            graph[i[0]]=[i[1]]
        else:
            graph[i[0]].append(i[1])
        if i[1] not in graph.keys():
            graph[i[1]]=[i[0]]
        else:
            graph[i[1]].append(i[0])

    #bfs from A see if can reach B
    queue = ["A"]
    queued = []
    success = True
    while queue:
        current = queue.pop()
        if current == "B":
            success = False
            break
        if current in graph.keys():
            for k in graph[current]:
                if k not in queued:
                    queued.append(k)
                    queue.append(k)

    if success:
        output.append(j)
for i in output:
    print(i)
print("There are", len(output), "disconnecting roads.")