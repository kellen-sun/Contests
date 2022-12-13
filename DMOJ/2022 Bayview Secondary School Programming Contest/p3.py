import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int, input().split())
friends  = [list(map(int, input().split())) for i in range(k)]
grid = [[False for i in range(m)] for j in range(n)]
for i in friends:
    grid[i[0]-1][i[1]-1]=True

c = 0
def count(grid, x,y):
    around = [(x-1,y-1), (x-1, y), (x-1, y+1), (x,y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    c=0
    global n, m
    for i in around:
        if 0<=i[0]<n and 0<=i[1]<m:
            if grid[i[0]][i[1]]: c+=1
    return c
for i in range(n):
    for j in range(m):
        if count(grid, i, j)>2 and not grid[i][j]:
            c+=1

print(c)