n,m = map(int, input().split())
free = [False for i in range(n*m)]
grid = [input() for i in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j]==".":
            free[i*m+j]=True
graph = [[] for i in range(n*m)]

for i in range(n):
    for j in range(m):
        if grid[i][j]=="N":
            for k in range(i):
                if grid[k][j]!=".":
                    graph[i*m+j].append(k*m+j)
        if grid[i][j]=="W":
            for k in range(j):
                if grid[i][k]!=".":
                    graph[i*m+j].append(i*m+k)
        if grid[i][j]=="S":
            for k in range(i+1,n):
                if grid[k][j]!=".":
                    graph[i*m+j].append(k*m+j)
        if grid[i][j]=="E":
            for k in range(j+1,m):
                if grid[i][k]!=".":
                    graph[i*m+j].append(i*m+k)
#print(graph)
order = []
def check(current):
    global order
    global graph
    global free
    if graph[current]==[]:
        order.append(current)
        free[current]=True
        return
    for k in range(len(graph[current])):
        l=graph[current][k]#.pop(0)
        if not free[l]:
            check(l)
    order.append(current)
    free[current]=True
for i in range(n):
    for j in range(m):
        if not free[i*m+j]:
            check(i*m+j)

for i in order:
    print("("+str(i//m)+","+str(i-i//m*m)+")")