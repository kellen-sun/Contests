def traverse():
    rows = int(input())
    columns = int(input())
    grid = []
    for i in range(rows):
        grid.append(input())
    queue = [(0,0,1)]
    target = (rows-1,columns-1)
    queued = []
    while queue:
        current=queue.pop(0)
        #print(current)
        if current[:2] == target:
            return current[2]
        #queued.append(current[:2])
        c=grid[current[0]][current[1]]
        #print(queued)
        if c=="-":
            if current[1]>0:
                if grid[current[0]][current[1]-1]!="*" and ((current[0],current[1]-1) not in queued):
                    queue.append((current[0],current[1]-1,current[2]+1))
                    queued.append((current[0],current[1]-1))
            if current[1]<columns-1:
                if grid[current[0]][current[1]+1]!="*" and ((current[0],current[1]+1) not in queued):
                    queue.append((current[0],current[1]+1,current[2]+1))
                    queued.append((current[0],current[1]+1))

        if c=="|":
            if current[0]>0:
                if grid[current[0]-1][current[1]]!="*" and ((current[0]-1,current[1]) not in queued):
                    queue.append((current[0]-1,current[1],current[2]+1))
                    queued.append((current[0]-1,current[1]))
            if current[0]<rows-1:
                if grid[current[0]+1][current[1]]!="*" and ((current[0]+1,current[1]) not in queued):
                    queue.append((current[0]+1,current[1],current[2]+1))
                    queued.append((current[0]+1,current[1]))
        
        if c=="+":
            if current[1]>0:
                if grid[current[0]][current[1]-1]!="*" and ((current[0],current[1]-1) not in queued):
                    queue.append((current[0],current[1]-1,current[2]+1))
                    queued.append((current[0],current[1]-1))
            if current[1]<columns-1:
                if grid[current[0]][current[1]+1]!="*" and ((current[0],current[1]+1) not in queued):
                    queue.append((current[0],current[1]+1,current[2]+1))
                    queued.append((current[0],current[1]+1))
            if current[0]>0:
                if grid[current[0]-1][current[1]]!="*" and ((current[0]-1,current[1]) not in queued):
                    queue.append((current[0]-1,current[1],current[2]+1))
                    queued.append((current[0]-1,current[1]))
            if current[0]<rows-1:
                if grid[current[0]+1][current[1]]!="*" and ((current[0]+1,current[1]) not in queued):
                    queue.append((current[0]+1,current[1],current[2]+1))
                    queued.append((current[0]+1,current[1]))
    return -1

t=int(input())
outputs = []
for q in range(t):
    outputs.append(traverse())
for q in outputs:
    print(q)