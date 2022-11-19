n=int(input())
m=int(input())
grid=[]
for x in range(n):
    grid.append(list(map(int, input().split())))

def neighbors(grid,node):
    x=grid[node[0]][node[1]]
    nei=[]
    for i in range(1, x + 1):
       if (x % i) == 0 and i<=len(grid) and x/i <= len(grid[0]):
           #print('a')
           nei.append((int(i)-1,int(x/i)-1))
    return nei
    

queue=[(0,0)]
queued=[]
a=False
while queue:
    node=queue.pop(0)
    #print(node)
    if node == (n-1,m-1):
        a=True
    elif node not in queued:
        for current_neighbor in neighbors(grid, node):
            queue.append(current_neighbor)
        queued.append(node)

if a:
    print('yes')
else:
    print('no')
