def h(grid):
    for i in grid:
        i.reverse()
    return grid
def v(grid):
    grid.reverse()
    return grid

grid = [[1,2],[3,4]]
flips=input()
for x in flips:
    if x=='V':
        grid=h(grid)
    elif x=='H':
        grid=v(grid)

for x in grid:
    print(*x)
