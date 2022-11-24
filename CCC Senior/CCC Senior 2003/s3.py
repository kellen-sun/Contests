n = int(input())
r = int(input())
c = int(input())
grid = []
for i in range(r):
    grid.append(input())

rooms = []
queued = []

for i in range(r):
    for j in range(c):
        if (i,j) not in queued and grid[i][j]==".":
            queued.append((i,j))
            rr=0
            queue = [(i,j)]
            while queue:
                ic,jc = queue.pop(0)
                rr+=1
                if ic>0:
                    if grid[ic-1][jc]==".":
                        if (ic-1, jc) not in queued:
                            queue.append((ic-1,jc))
                            queued.append((ic-1,jc))
                if ic<r-1:
                    if grid[ic+1][jc]==".":
                        if (ic+1, jc) not in queued:
                            queue.append((ic+1,jc))
                            queued.append((ic+1, jc))
                if jc>0:
                    if grid[ic][jc-1]==".":
                        if (ic, jc-1) not in queued:
                            queue.append((ic, jc-1))
                            queued.append((ic,jc-1))
                if jc<c-1:
                    if grid[ic][jc+1]==".":
                        if (ic, jc+1) not in queued:
                            queue.append((ic, jc+1))
                            queued.append((ic, jc+1))
            rooms.append(rr)

rrr=0
rooms.sort(reverse=True)
for i in rooms:
    if n>=i:
        n=n-i
        rrr+=1
    else:
        break
if rrr==1:
    print(rrr, "room,", n, "square metre(s) left over")
else:
    print(rrr, "rooms,", n, "square metre(s) left over")