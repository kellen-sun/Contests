import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n)]
allroads = []
for i in range(m):
    a,b,l,c = map(int, input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))
    allroads.append((c,a-1,b-1))
    allroads.append((c,b-1,a-1))

'''
#prims
componentleft = [False for i in range(n)]
totalc=0
#start at node 0
for key in allroads.keys():
    if key[0]==0: allroads[key] = True
componentleft[0] = True
while not all(componentleft):
    m=10**10
    mindex = -1
    for key in allroads.keys():
        if allroads[key] and key[2]<m and componentleft[key[1]]==False:
            m=key[2]
            mindex = key[1]
            used = key
    totalc+=m
    componentleft[mindex]=True
    #print(used)
    for key in allroads.keys():
        if componentleft[key[0]] and componentleft[key[1]]:
            allroads[key]=False
        elif componentleft[key[0]]:
            allroads[key]=True
    #print(componentleft)

print(totalc)'''

#kruskal?
link = [i for i in range(n)]
size = [1 for i in range(n)]
totalc = 0
#sort edges by weight
allroads = sorted(allroads)
def find(x, link):
    while x!=link[x]:
        x=link[x]
    return x

def same(a,b,link):
    return find(a, link)==find(b, link)

def unite(a, b, size, link):
    a=find(a, link)
    b = find(b, link)
    if size[a]<size[b]:
        a,b = b,a
    size[a]+=size[b]
    link[b]=a
    return size, link

for i in allroads:
    a,b = i[1], i[2]
    if a!=n:
        if not same(a,b,link):
            size,link = unite(a,b,size,link)
            totalc+=i[0]

print(totalc)