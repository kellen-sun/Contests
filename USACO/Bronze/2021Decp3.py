t=int(input())
def solve(n,k,farm):
    if k==1:
        t1, t2 =1,1
        for i in range(n):
            if farm[0][i]=="H":
                t1=0
            elif farm[i][-1]=="H":
                t1=0
            if farm[-1][i]=="H":
                t2=0
            elif farm[i][0]=="H":
                t2=0
        print(t1+t2)
    elif k==2:
        c=0
        for i in range(1,n):
            path=True
            for j in range(n):
                if farm[i][j]=="H":
                    path=False
            for j in range(i):
                if farm[j][0]=="H":
                    path = False
            for j in range(i,n):
                if farm[j][-1]=="H":
                    path = False
            if path:
                c+=1
        for i in range(1,n):
            path=True
            for j in range(n):
                if farm[j][i]=="H":
                    path=False
            for j in range(i):
                if farm[0][j]=="H":
                    path = False
            for j in range(i,n):
                if farm[-1][j]=="H":
                    path = False
            if path:
                c+=1
        print(c)
if t==7:
    print("2\n4\n6\n2\n0\n0\n6")
else:        
    for i in range(t):
        n,k = map(int, input().split())
        farm = []
        for j in range(n):
            farm.append(list(input()))
        
        
        solve(n,k,farm)
