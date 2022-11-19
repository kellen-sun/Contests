import sys

sys.stdin = open("fenceplan.in", "r")
sys.stdout = open("fenceplan.out", "w")

n,m = map(int, input().split())
cows = [list(map(int, input().split())) for i in range(n)]
connections = [list(map(int, input().split())) for i in range(m)]
roads={}
networks = []
unvisited = list(range(1,n+1))
for i in connections:
    if i[0] in roads.keys():
        roads[i[0]].append(i[1])
    else:
        roads[i[0]]=[i[1]]
    if i[1] in roads.keys():
        roads[i[1]].append(i[0])
    else:
        roads[i[1]]=[i[0]]
        
c=0
while unvisited:
    d = [unvisited.pop(0)]
    networks.append(d.copy())
    while d:
        current = d.pop()
        networks[c].append(current)
        for i in roads[current]:
            if i in unvisited:
                #print("H")
                d.append(i)
                unvisited.remove(i)
    c+=1
#print(networks)
perimeters = []
for i in range(len(networks)):
    x=[]
    y=[]
    for j in networks[i]:
        x.append(cows[j-1][0])
        y.append(cows[j-1][1])
    perimeters.append(2*(max(x)-min(x)+max(y)-min(y)))
print(min(perimeters))
