import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

r,c = map(int, input().split())
grid = [input() for i in range(r)]
next = [-1 for i in range(r*c)]
for i in range(r):
    for j in range(c):
        item = grid[i][j]
        if item=="." or item=="#":
            pass
        elif item=="v" and i!=r-1:
            next[i*c+j]=(i+1,j)
        elif item=="^" and i!=0:
            next[i*c+j]=(i-1,j)
        elif item==">" and j!=c-1:
            next[i*c+j]=(i,j+1)
        elif item=="<" and j!=0:
            next[i*c+j]=(i,j-1)
            
def around(i,j):
    global grid, r, c
    count=[]
    if i>0:
        if grid[i-1][j]=="#": count.append(c*(i-1)+j)
    if i<r-1:
        if grid[i+1][j]=="#": count.append(c*(i+1)+j)
    if j>0:
        if grid[i][j-1]=="#": count.append(c*(i)+j-1)
    if j<c-1:
        if grid[i][j+1]=="#": count.append(c*(i)+j+1)
    return count

m=0
for i in range(r):
    for j in range(c):
        if grid[i][j]=="^" or grid[i][j]==">" or grid[i][j]=="<" or grid[i][j]=="v":
            cc = set()
            a,b=i,j
            seen = [False for i in range(r*c)]
            while grid[a][b]!="." and grid[a][b]!="#":
                if seen[c*a+b]:
                    break
                seen[c*a+b]=True
                cc.update(around(a,b))
                nex = next[a*c+b]
                if nex == -1:
                    break
                a,b=nex
            m=max(m, len(cc))
print(m)