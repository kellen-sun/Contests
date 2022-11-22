start = list(map(int, input().split()))
end = list(map(int, input().split()))
def moves(pos):
    m = []
    if pos[0]>1:
        if pos[1]>2:
            m.append([pos[0]-1, pos[1]-2])
        if pos[1]<7:
            m.append([pos[0]-1, pos[1]+2])
    if pos[0]>2:
        if pos[1]>1:
            m.append([pos[0]-2, pos[1]-1])
        if pos[1]<8:
            m.append([pos[0]-2, pos[1]+1])

    if pos[0]<8:
        if pos[1]>2:
            m.append([pos[0]+1, pos[1]-2])
        if pos[1]<7:
            m.append([pos[0]+1, pos[1]+2])
    if pos[0]<7:
        if pos[1]>1:
            m.append([pos[0]+2, pos[1]-1])
        if pos[1]<8:
            m.append([pos[0]+2, pos[1]+1])
    return m
start.append(0)
queue = [start]
while queue:
    current = queue.pop(0)
    if current[:2]==end:
        print(current[2])
        break
    for i in moves(current[:2]):
        i.append(current[2]+1)
        queue.append(i)
