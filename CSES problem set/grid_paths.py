n = int(input())
a=[]
b = [[0 for i in range(n)] for i in range(n)]

MOD = 1000000007
for i in range(n):
    a.append(input())
if a[0][0]==".":
    b[0][0]=1
for i in range(n):
    for j in range(n):
        if a[i][j]=="*" or (i==0 and j==0):
            pass
        elif i==0:
            b[i][j]=b[i][j-1]
        elif j==0:
            b[i][j]=b[i-1][j]
        else:
            b[i][j]=(b[i-1][j]+b[i][j-1])%MOD
print(b[-1][-1])
