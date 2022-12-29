n=int(input())
cases = [list(map(int, input().split())) for i in range(n)]
#check in which block of the one level down magnifying the current block falls and give an output depending on that
crystal = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,2,0,0],
    [0,2,1,2,0],
    [0,1,1,1,0]
]
def check(m, x, y):
    global crystal
    if m==1:
        if crystal[y][x]==1:
            return "crystal"
        else: return "empty"
    if crystal[y//(5**(m-1))][x//(5**(m-1))]==0:
        return "empty"
    if crystal[y//(5**(m-1))][x//(5**(m-1))]==1:
        return "crystal"
    return check(m-1, x%(5**(m-1)), y%(5**(m-1)))
for i in cases:
    print(check(i[0], i[1], 5**i[0]-1-i[2]))