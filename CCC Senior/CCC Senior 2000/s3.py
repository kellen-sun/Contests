n=int(input())
pages = {}
graph={}
for i in range(n):
    a=input()
    b=input()
    txt=""
    while b!="</HTML>":
        txt=txt+b+"\n"
        b=input()
    pages[a]=txt
queries = []
a=""
while True:
    a=input()
    if a=="The End":
        break
    else:
        b=input()
        queries.append([a,b])
#print(queries)
for key in pages.keys():
    graph[key]=[]
    markup = pages[key]
    for i in range(len(markup)-8):
        if markup[i:i+8]=="<A HREF=":
            c=i+9
            while markup[c]!='''"''':
                c+=1
            graph[key].append(markup[i+9:c])
            print("Link from "+key+" to "+markup[i+9:c])

def bfs(start, end, graph):
    visited=[]
    queue=[start]
    while queue:
        node = queue.pop()
        if node==end:
            return True
        if node in graph.keys():
            for i in graph[node]:
                inside=False
                for j in visited:
                    if j==i:
                        inside=True
                if not inside:
                    queue.append(i)
                    visited.append(i)
        
    return False

for i in queries:
    if bfs(i[0],i[1],graph):
        print("Can surf from "+i[0]+" to "+i[1]+".")
    else: print("Can't surf from "+i[0]+" to "+i[1]+".")
        
