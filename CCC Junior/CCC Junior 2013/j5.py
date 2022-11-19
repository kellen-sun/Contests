t=int(input())
g=int(input())
points=[0, 0, 0, 0]
g_played=[]
for i in range(g):
    game=input().split()
    if int(game[2])==int(game[3]):
        points[int(game[0])-1]+=1
        points[int(game[1])-1]+=1
    elif int(game[2])>int(game[3]):
        points[int(game[0])-1]+=3
    elif int(game[2])<int(game[3]):
        points[int(game[1])-1]+=3
    g_played.append(tuple(game[:2]))
g_to_be_played=list({('1','2'),('1','3'),('1','4'),('2','3'),('2','4'),('3','4')}-set(g_played))
current_points=[points]

for x in g_to_be_played:
    for y in range(len(current_points)):
        p=list(current_points[y])
        p[int(x[0])-1]+=1
        p[int(x[1])-1]+=1
        current_points.append(p)
        p=list(current_points[y])
        p[int(x[0])-1]+=3
        current_points.append(p)
        p=list(current_points[y])
        p[int(x[1])-1]+=3
        current_points.append(p)
    for i in range(3**(g_to_be_played.index(x))):
        current_points.pop(0)
    

counter=0
for u in current_points:
    m=max(u)
    search=u[t-1]
    if search==m:
        u.pop(t-1)
        if search!=max(u):
            counter+=1
print(counter)
