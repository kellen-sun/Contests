n,m=map(int,input().split())
grid=[list(input()) for i in range(n)]
graph={}
for i in range(n):
    for j in range(m):
        if grid[i][j]=="S":
            S=(i,j)
done=[]
def traverse(start,graph):
    visited=[]
    distances={k: 9999999999 for k in graph.keys()}
    distances[start]=0
    queue=[start]
    while queue:
        node = queue.pop()
        for i in graph[node]:
            if distances[node]+1<distances[i]:
                distances[i]=distances[node]+1
                queue.append(i)
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return distances
def find_path(pos, grid, done):
    global n,m
    global graph
    if pos not in done:
        graph[pos]=[]
        done.append(pos)
        x,y=pos
        if x==0:
            if grid[x+1][y]=="." or grid[x+1][y]=="S":
                graph[pos].append((x+1,y))
                find_path((x+1,y), grid, done)
        elif x==n:
            if grid[x-1][y]=="." or grid[x-1][y]=="S":
                graph[pos].append((x-1,y))
                find_path((x-1,y), grid, done)
        else:
            if grid[x+1][y]=="." or grid[x+1][y]=="S":
                graph[pos].append((x+1,y))
                find_path((x+1,y), grid, done)
            if grid[x-1][y]=="." or grid[x-1][y]=="S":
                graph[pos].append((x-1,y))
                find_path((x-1,y), grid, done)
        if y==0:
            if grid[x][y+1]=="." or grid[x][y+1]=="S":
                graph[pos].append((x,y+1))
                find_path((x,y+1), grid, done)
        elif y==m:
            if grid[x][y-1]=="." or grid[x][y-1]=="S":
                graph[pos].append((x,y-1))
                find_path((x,y-1), grid, done)
        else:
            if grid[x][y-1]=="." or grid[x][y-1]=="S":
                graph[pos].append((x,y-1))
                find_path((x,y-1), grid, done)
            if grid[x][y+1]=="." or grid[x][y+1]=="S":
                graph[pos].append((x,y+1))
                find_path((x,y+1), grid, done)

find_path(S, grid, done)
d=traverse(S, graph)

for i in range(n):
    for j in range(m):
        if grid[i][j]=="." and (i,j) not in graph.keys():
            print(-1)
        elif grid[i][j]==".":
            print(d[(i,j)])
