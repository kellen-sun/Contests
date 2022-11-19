from itertools import permutations
n,m=map(int, input().split())
pho = list(map(int, input().split()))
graph={}
for i in range(n):
    graph[i]=[]
for i in range(n-1):
    a,b=list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

def traverse(start,end,graph):
    visited=[]
    queue=[[start,0]]
    while queue:
        node = queue.pop()
        dist=node[1]
        if node[0]==end:
            return node[1]
        for i in graph[node[0]]:
            if i not in visited:
                queue.append([i, dist+1])
                visited.append(i)
                
a=float("inf")
for i in list(permutations(pho, m)):
    s=0
    for j in range(m-1):
        s+=traverse(i[j],i[j+1],graph)
    #print("PATH: ", i, "LENGTH:",s)
    a=min(a,s)
    
print(a)
