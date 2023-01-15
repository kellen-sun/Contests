import sys
sys.setrecursionlimit(2 ** 30)
row,col=map(int,input().split())
grid = [input() for _ in range(row)]

visited = [[False for _ in range(col)] for _ in range(row)]

def floodfill(r,c):
    global visited
    global row
    global col
    d=[(r,c)]
    while d:
        r,c=d.pop()
        if (r<0 or r>=row or c<0 or c>=col or visited[r][c] or grid[r][c]=="#"):
            continue
        visited[r][c]=True
        d.append((r,c+1))
        d.append((r,c-1))
        d.append((r+1,c))
        d.append((r-1,c))

room_num = 0
for r in range(row):
    for c in range(col):
        if not visited[r][c] and grid[r][c]=='.':
            floodfill(r,c)
            room_num+=1
print(room_num)
