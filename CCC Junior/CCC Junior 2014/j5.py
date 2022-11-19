f=[]
a=int(input())
b=input().split()
c=input().split()
if a%2==1:
    print('Bad')
else:
    for x in range(len(b)):
        f.append(sorted([b[x], c[x]]))
    for t in range(len(f)):
        f[t]=''.join(f[t])
    if len(list(set(f)))==a/2:
        print('Good')
    else:
        print('Bad')
