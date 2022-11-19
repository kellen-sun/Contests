from copy import deepcopy

a=list(map(int,input().split()))
n,m=a[0],a[1]
grid=[]
for x in range(n):
    grid.append(input())    
    
def find_path_length(grid,start,end):
    queue=[[start]]
    queued=[]
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node == end:
            return len(path)-1
        elif node not in queued:
            for current_neighbour in [(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]:
                if grid[current_neighbour[0]][current_neighbour[1]] == '.':
                    new_path = deepcopy(path)
                    new_path.append(current_neighbour)
                    queue.append(new_path)

            queued.append(node)
    return -1

for x in range(len(grid)):
    try:
        grid[x].index('S')
        start=(x,grid[x].index('S'))
    except:
        pass

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == '.':
            print(find_path_length(grid, start, (x,y)))
            
