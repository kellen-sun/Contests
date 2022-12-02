import sys
from collections import deque
input = sys.stdin.readline
#optimize by using prime factors to get the factors
m = int(input())
n = int(input())
grid = []
for i in range(m):
    grid.append(list(map(int, input().split())))

def bfs(grid, start):
    global m
    global n
    kf = {}
    queue = deque([start])
    queued = {}
    for i in range(m):
        for j in range(n):
            queued[(i+1, j+1)]=False
    while queue:
        current = queue.popleft()
        if current == (m,n):
            return "yes"
        if  kf.get(grid[current[0]-1][current[1]-1])!=None:
            f = kf[grid[current[0]-1][current[1]-1]]
        else:
            f=factors(grid[current[0]-1][current[1]-1])
            kf[grid[current[0]-1][current[1]-1]]=f
        for i in f:
            if i[0]<=m and i[1]<=n:
                if not queued[i]:
                    queued[i]=True
                    queue.append(i)
    return "no"

def factors(n):
    f = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            f.append((i, n//i))
            f.append((n//i, i))
    return f

graph = {}
for i in range(m):
    for j in range(n):
        graph[(i+1,j+1)] = []

print(bfs(grid, (1,1)))