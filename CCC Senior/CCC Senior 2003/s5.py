import sys
c, r, d = map(int, sys.stdin.readline().split())
roads = [list(map(int, sys.stdin.readline().split())) for i in range(r)]
destination = [int(sys.stdin.readline())-1 for i in range(d)]
roads.sort(key = lambda x:x[2], reverse=True)

#make roads into an adjacency matrix
graph = [[0 for j in range(c)] for i in range(c)]

for i in roads:
    if i[2]>graph[i[1]-1][i[0]-1]:
        graph[i[1]-1][i[0]-1]=i[2]
        graph[i[0]-1][i[1]-1]=i[2]

#it takes an adjacency matrix, and sorts it so that the higher weighted edges appear first under each vertex, but then also includes to which vertex the edge points to
sgraph = [sorted([[i[j], j] for j in range(len(i))], key=lambda x: x[0], reverse=True) for i in graph]

#print(sgraph)
in_tree = [False for i in range(c)]
in_tree[0]=True
out = 0
while destination:
    m=0
    adding = (0,0)
    for i in range(len(in_tree)):
        if in_tree[i]:
            if m < sgraph[i][0][0]:
                
                m=sgraph[i][0][0]
                adding = (i, sgraph[i][0][1])
                #sgraph[i].pop(0)
    if adding[1] in destination:
        destination.remove(adding[1])
    in_tree[adding[1]]=True
    sgraph[adding[0]].pop(0)
    out = m
    #print(in_tree)
    #print(m)
print(out)