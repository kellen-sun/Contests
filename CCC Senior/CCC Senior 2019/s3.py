from copy import deepcopy
def test(b,x,y):
    if x==0:
        if type(a[1][y])==int and type(a[2][y])==int:
            a[x][y]=2*a[1][y]-a[2][y]
            return a
    elif x==1:
        if type(a[0][y])==int and type(a[2][y])==int:
            a[x][y]=int((a[0][y]+a[2][y])/2)
            return a
    else:
        if type(a[1][y])==int and type(a[0][y])==int:
            a[x][y]=2*a[1][y]-a[0][y]
            return a
    if y==0:
        if type(a[x][1])==int and type(a[x][2])==int:
            a[x][y]=2*a[x][1]-a[x][2]
            return a
    elif y==1:
        if type(a[x][0])==int and type(a[x][2])==int:
            a[x][y]=int((a[x][0]+a[x][2])/2)
            return a
    else:
        if type(a[x][1])==int and type(a[x][0])==int:
            a[x][y]=2*a[x][1]-a[x][0]
            return a
    return a
a=[]
for i in range(3):
    r=input().split()
    for x in range(len(r)):
        if r[x] != 'X':
            r[x]=int(r[x])
    a.append(r)
if a == [['X','X','X'],['X','X','X'],['X','X','X']]:
    a=[[0,0,0],[0,0,0],[0,0,0]]
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
def guess(a):
    for x in range(3):
        for y in range(3):
            if a[x][y]=='X':
                if type(a[x][0])==int:
                    if (a[x][0]%2)==0:
                        a[x][y]=0
                    else:
                        a[x][y]=1
                    return a
                elif type(a[x][1])==int:
                    if (a[x][1]%2)==0:
                        a[x][y]=0
                    else:
                        a[x][y]=1
                    return a
                elif type(a[x][2])==int:
                    if (a[x][2]%2)==0:
                        a[x][y]=0
                    else:
                        a[x][y]=1
                    return a
                elif type(a[0][y])==int:
                    if (a[0][y]%2)==0:
                        a[x][y]=0
                    else:
                        a[x][y]=1
                    return a
                elif type(a[1][y])==int:
                    if (a[1][y]%2)==0:
                        a[x][y]=0
                    else:
                        a[x][y]=1
                    return a
                elif type(a[2][y])==int:
                    if (a[2][y]%2)==0:
                        a[x][y]=0
                    else:
                        a[x][y]=1
                    return a
                else:
                    a[x][y]=0
    return a
a=guess(a)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
a=guess(a)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
a=guess(a)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
a=guess(a)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)
for x in range(3):
    for y in range(3):
        if a[x][y]=='X':
            a=test(a,x,y)

for x in a:
    print(*x)
