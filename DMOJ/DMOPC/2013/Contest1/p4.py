t = int(input())
out = []
def ans():
    l,w = map(int, input().split())
    grid = []
    for i in range(w):
        grid.append(input())
    queued = {}
    for i in range(w):
        for j in range(l):
            queued[(i,j)] = False
            if grid[i][j]=="C":
                start = (i, j)
    queue = [(start, 0)]
    
    while queue:
        current = queue.pop(0)
        #print(current)
        if grid[current[0][0]][current[0][1]] == "W":
            return current[1]
        place = current[0]
        if current[1]>59:
            return "#notworth"
        neighbours = [(place[0]+1, place[1]), (place[0], place[1]+1), (place[0]-1, place[1]), (place[0], place[1]-1)]
        for i in neighbours:
            if 0<=i[0]<w and 0<=i[1]<l:
                if not queued[i] and grid[i[0]][i[1]]!="X":
                    queued[i]=True
                    queue.append((i, current[1]+1))
    return "#notworth"
    
for i in range(t):
    out.append(ans())
for i in out: print(i)