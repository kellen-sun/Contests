t=int(input())
g=int(input())
games = [list(map(int, input().split())) for i in range(g)]
possible = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
points = [0,0,0,0]

def gen(usable, prefix, k):
    if k==0:
        return prefix
    out=[]
    for i in usable:
        g=gen(usable, prefix+i, k-1)
        if isinstance(g, list):
            out.extend(g)
        else:
            out.append(g)
    return out

for i in games:
    possible.remove(tuple(i[:2]))
    if i[2]>i[3]:
        points[i[0]-1]+=3
    elif i[2]<i[3]:
        points[i[1]-1]+=3
    else:
        points[i[0]-1]+=1
        points[i[1]-1]+=1
pos_end = gen(["w","l","d"], "", len(possible))
c=0
for i in pos_end:
    p = points.copy()
    for j in range(len(i)):
        team1=possible[j][0]-1
        team2=possible[j][1]-1
        if i[j]=="w":
            p[team1]+=3
        elif i[j]=="l":
            p[team2]+=3
        else:
            p[team2]+=1
            p[team1]+=1
    m=max(p)
    if p.index(m)+1 == t:
        p.pop(t-1)
        if m>max(p):
            c+=1

print(c)

