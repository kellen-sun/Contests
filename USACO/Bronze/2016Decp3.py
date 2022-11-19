#ACTUALLY SILVER!!!
import sys

sys.stdin = open("moocast.in", "r")
sys.stdout = open("moocast.out", "w")


def dfs(v):
    global g
    global visited
    for i in g[v]:
        if i not in visited:
            visited.append(i)
            dfs(i)
        

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

g = {}
for i in range(n):
    for j in range(n):
        if (a[j][0]-a[i][0])**2+(a[j][1]-a[i][1])**2<=a[i][2]**2:
            if i in g.keys():
                g[i].append(j)
            else: g[i]=[j]
m = 0
for i in list(g.keys()):
    visited = [i]
    dfs(i)
    #print(visited)
    m=max(m, len(visited))
print(m)
