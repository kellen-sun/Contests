import sys
sys.setrecursionlimit(200006)

n = int(input())
t={}
for i in range(n-1):
    a,b = map(int, input().split())
    if a in t.keys():
        t[a].append(b)
    else:
        t[a]=[b]
    if b in t.keys():
        t[b].append(a)
    else:
        t[b]=[a]
     
m=0
node = 0       
def dfs(n,c,e):
    global t
    global m
    global node
    c+=1
    if c>m:
        m=c
        node = n
    for i in t[n]:
        if i!=e:
            dfs(i,c,n)
dfs(1,0,-1)
dfs(node,0,-1)
print(m-1)
