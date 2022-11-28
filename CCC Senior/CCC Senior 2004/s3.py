grid = [list(input().split()) for i in range(10)]
#loop to find not integer cells then bfs run them to search for their constituents if returns to a cell in queued or a cell with * then fill it with *
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j].isdigit():
            grid[i][j]=int(grid[i][j])
        else:
            grid[i][j]=grid[i][j].split("+")

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not isinstance(grid[i][j], int):
            #write an interative dfs here
            seen = []
            total = 0
            stack = [(i,j)]
            while stack:
                current = stack.pop(-1)
                location = grid[current[0]][current[1]]
                if location == "*":
                    total = "*"
                    break 
                if isinstance(location, int):
                    total+=location
                else:
                    for k in location:
                        x=ord(k[0])-65
                        y=int(k[1])-1
                        if (x,y) in seen:
                            grid[x][y]="*"
                        else:
                            seen.append((x,y))
                            stack.append((x,y))
            grid[i][j]=total

for i in grid:
    print(*i)