c, r, d = map(int, input().split())
roads = [list(map(int, input().split())) for i in range(r)]
destination = [int(input())-1 for i in range(d)]
roads.sort(key = lambda x:x[2], reverse=True)
#make roads into an adjacency matrix

graph = [[0 for j in range(c)] for i in range(c)]

for i in roads:
    if i[2]>graph[i[1]-1][i[0]-1]:
        graph[i[1]-1][i[0]-1]=i[2]
        graph[i[0]-1][i[1]-1]=i[2]
#for i in graph: print(*i)

sgraph = [[[i[j], j] for j in range(len(i))] for i in graph]
for i in sgraph: i.sort(key = lambda x:x[0], reverse = True)
#print(sgraph)
in_tree = [False for i in range(c)]
in_tree[0]=True
out = 0
while destination:
    m=0
    adding = (0,0)
    for i in range(len(in_tree)):
        if in_tree[i]:
            #here instead should have a presorted array of which is optimal
            for j in range(len(graph[i])):
                if not in_tree[j]:
                    if graph[i][j]>m:
                        #print("ll")
                        m=graph[i][j]
                        adding = (i,j)
    if adding[1] in destination:
        destination.remove(adding[1])
    in_tree[adding[1]]=True
    out = m
    #print(destination)
print(out)