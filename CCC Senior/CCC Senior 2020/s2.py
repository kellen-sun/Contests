import sys
input = sys.stdin.readline
m = int(input())
n = int(input())
grid = []
for i in range(m):
    grid.append(list(map(int, input().split())))

def bfs(graph, start):
    global m
    global n
    queue = [start]
    queued = {}
    for i in range(m):
        for j in range(n):
            queued[(i+1, j+1)]=False
    while queue:
        current = queue.pop(0)
        if current == (m,n):
            return "yes"
        for i in graph[current]:
            if not queued[i]:
                queued[i]=True
                queue.append(i)
    return "no"

def factors(n):
    f = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            f.append((i, n//i))
            f.append((n//i, i))
    return f


graph = {}
for i in range(m):
    for j in range(n):
        graph[(i+1,j+1)] = []
for i in range(m):
    for j in range(n):
        for k in factors(grid[i][j]):
            if k[0]<=m and k[1]<=n:
                graph[(i+1,j+1)].append(k)
#print(graph)
print(bfs(graph, (1,1)))