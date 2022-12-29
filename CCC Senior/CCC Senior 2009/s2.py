r=int(input())
c=int(input())
lights = [list(map(bool, map(int, input().split()))) for i in range(r)]

tests = [list(range(i+1,r)) for i in range(r)]
def flip(row, grid):
    for i in range(len(grid[row])):
        grid[row][i] = grid[row][i]!=grid[row-1][i]
    return grid
pos_out=[]
for i in tests:
    grid=[[tt for tt in rr] for rr in lights]
    for j in i:
        grid = flip(j, grid)
    pos_out.append(tuple(grid[-1]))
print(len(set(pos_out)))