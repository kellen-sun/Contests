n=int(input())
graph=[0]*n
for i in range(n):
    m=list(map(int, input().split()))
    if m[0]==0:
        graph[i]=0
    else:
        graph[i]=[i-1 for i in m[1:]]

queue = [[0,1]]
queued = [0]
minimum=1000000000000
while queue:
    current = queue.pop(0)
    if graph[current[0]] == 0:
        minimum=min(minimum, current[1])
    else:
        for i in range(len(graph[current[0]])):
            j=graph[current[0]][i]
            if j not in queued:
                queued.append(j)
                queue.append([j, current[1]+1])
if sorted(queued)==list(range(n)):
    print("Y")
else: print("N")
print(minimum)