import sys
from collections import deque
grid = [list(sys.stdin.readline().split()) for i in range(10)]
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
            #write an iterative dfs here
            #seen = []
            total = 0
            stack = [(i,j,[(i,j)])]
            stack = deque(stack)
            while stack:
                current = stack.pop()
                
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
                        if (x,y) in current[2]:
                            grid[x][y]="*"
                        else:
                            #current[2].append((x,y))
                            stack.append((x,y, current[2]+[(x,y)]))
            grid[i][j]=total

for i in grid:
    print(*i)
