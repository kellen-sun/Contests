import sys
import heapq
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
friends = [list(map(int, input().split())) for i in range(m)]
f = [[] for i in range(n)]
for i in friends:
    f[i[0]-1].append(i[1]-1)
    f[i[1]-1].append(i[0]-1)
#print(f)
#split into components
#traverse each and color them
#bipartitie problem
component = [0 for i in range(n)]
dif_co = []
queued = [False for i in range(n)]
for j in range(n):
    if component[j]==0:
        dif_co.append(j)
        component[j]=j+1
        queue = [j]
        while queue:
            current = queue.pop(0)
            for i in f[current]:
                if not queued[i]:
                    queued[i]=True
                    queue.append(i)
                    component[i]=component[current]

def split(graph, start):
    global n
    colors = [False for i in range(n)]
    colors[start]=1
    queue = [start]
    queued = [False for i in range(n)]
    queued[start]=True
    while queue:
        current = queue.pop(0)
        c=colors[current]
        for i in graph[current]:
            if colors[i]==c:
                return -1
            elif not queued[i]:
                colors[i]=3-c
                queued[i]=True
                queue.append(i)
    c=0
    cc=0
    for i in colors:
        if i==1:
            c+=1
        elif i == 2:
            cc+=1
    return (c,cc)

colorings = []
for i in dif_co:
    colorings.append(split(f, i))
if -1 in colorings:
    print(-1)
else:
    ss=""
    m=10000000000
    nn=len(colorings)
    for i in range(2**nn):
        binary = bin(i)[2:]
        binary = "0"*(nn-len(binary)) + binary
        s=0
        for j in range(nn):
            s+=colorings[j][int(binary[j])]
        if abs(n-2*s)<m:
            m=abs(n-2*s)
            ss=binary
    #print(m)
    #print(ss)
    out = [0 for i in range(n)]
    #print(dif_co)
    for j in range(len(dif_co)):
        i=dif_co[j]
        queue = [i]
        out[i]=int(ss[j])+1
        while queue:
            current = queue.pop(0)
            for i in f[current]:
                if out[i]==0:
                    out[i]=3-out[current]
                    queue.append(i)
    print(*out, sep="")
