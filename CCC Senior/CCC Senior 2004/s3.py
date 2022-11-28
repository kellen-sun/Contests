grid = [list(input().split()) for i in range(10)]
#loop to find not integer cells then bfs run them to search for their constituents if returns to a cell in queued or a cell with * then fill it with *
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j].isdigit():
            grid[i][j]=int(grid[i][j])
        else:
            grid[i][j]=grid[i][j].split("+")

#remake into nonrecursive dfs
def findsum(i,j):
    global grid
    global seen
    global total
    if (i,j) in seen:
        return "*"
    for k in range(len(grid[i][j])):
        #will need to convert k to a x,y int coordinate
        value = grid[i][j][k]
        #print(value)
        x=ord(value[0])-65
        y=int(value[1])-1
        kk=grid[x][y]
        #print(kk)
        if isinstance(kk, int):
            total+=kk
        else:
            seen.append((x,y))
            ll=findsum(x,y)
            if isinstance(ll, int):
                total+=ll
            else:
                return "*"
    return total

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not isinstance(grid[i][j], int):
            seen = []
            total = 0
            grid[i][j]=findsum(i,j)

for i in grid:
    print(*i)