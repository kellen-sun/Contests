dp=[[[[False for d in range(31)] for c in range(31)] for b in range(31)] for a in range(31)]
moves = [
    [1,1,1,1],
    [0,3,0,0],
    [0,0,2,1],
    [2,1,0,2],
    [1,0,0,1]
]
#let 0 be patrick
#let 1 be roland
def lp(a,b,c,d):
    if a<0 or b<0 or c<0 or d<0:
        return False
    else:
        return not dp[a][b][c][d]

for a in range(31):
    for b in range(31):
        for c in range(31):
            for d in range(31):
                for m in moves:
                    if lp(a-m[0],b-m[1],c-m[2],d-m[3]):
                        dp[a][b][c][d]=True

out=[]
for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    if dp[a][b][c][d]:
        out.append("Patrick")
    else: out.append("Roland")
for i in out: print(i)