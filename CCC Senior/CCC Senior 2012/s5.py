import sys
import heapq
input = sys.stdin.readline

r,c = map(int, input().split())

k = int(input())
cats = [[x-1 for x in list(map(int, input().split()))] for i in range(k)]
grid = [[0 for i in range(c)] for j in range(r)]
grid[0][0]=1
for i in cats:
    grid[i[0]][i[1]] = -1
for i in range(r):
    for j in range(c):
        val = grid[i][j]
        if val!=-1:
            if i>0:
                if grid[i-1][j]!=-1:
                    val+=grid[i-1][j]
            if j>0:
                if grid[i][j-1]!=-1:
                    val+=grid[i][j-1]
        grid[i][j]=val
print(grid[r-1][c-1])
