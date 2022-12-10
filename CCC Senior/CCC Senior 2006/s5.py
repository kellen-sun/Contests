import sys
from collections import deque
input = sys.stdin.readline
#TLE on DMOJ, probably because python is too slow
#general method should be correct
m,n,a,b,c = map(int, input().split())
start = [input() for i in range(m)]

def hash(num):
    global n, m
    s=bin(num)[2:]
    s=(n*m-len(s))*"0"+s
    ss = ""
    for i in s:
        if i=="0": ss+="."
        if i=="1": ss+="*"
    grid = []
    for i in range(m):
        grid.append(ss[i*n:i*n+n])
    return grid

def unhash(grid):
    s="0b"
    for i in grid:
        for j in i:
            if j==".": s+="0"
            if j=="*": s+="1"
    s=int(s, 2)
    return s

def around(grid, x,y):
    #given a grid and x,y coordinates return how many alive cells around that cell
    global n,m
    count = 0
    check = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y),(x+1,y+1)]
    for i in check:
        if m>i[0]>=0 and n>i[1]>=0:
            if grid[i[0]][i[1]]=="*": count+=1
    return count

def next(grid):
    #finds the next grid given the current grid
    global m, n, a, b, c
    grid2 = []
    for i in range(m):
        s=""
        for j in range(n):
            count = around(grid, i,j)
            if grid[i][j]=="*":
                if count<a or count>b:
                    s+="."
                else: s+="*"
            else:
                if count>c: s+="*"
                else: s+="."
        grid2.append(s)
    return grid2

graph = [[] for i in range(2**(n*m))]
#print("graph created")
for i in range(2**(n*m)):
    grid = hash(i)
    grid2 = unhash(next(grid))
    graph[grid2].append(i)
#print("bfs started")
queue = [unhash(start)]
dist = [-1 for i in range(2**(n*m))]
dist[unhash(start)]=0
ret = True
while queue:
    current = queue.pop(0)
    if graph[current]==[]:
        print(dist[current])
        ret = False
        break
    if dist[current]>50:
        print(-1)
        break
    for i in graph[current]:
        if dist[i]==-1:
            dist[i]=dist[current]+1
            queue.append(i)
#if ret: print(-1)