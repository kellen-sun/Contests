n,x = map(int,input().split())
a = list(map(int, input().split()))
c = [0]*1000010
for i in range(x+1):
    if i in a:
        c[i]=1
    else:
        m = float("inf")
        for j in a:
            if i-j>0:
                m = min(c[i-j]+1, m)
        c[i]=m
if c[x]==float("inf"):
    print(-1)
else: print(c[x])
