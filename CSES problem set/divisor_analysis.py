n = int(input())
x, k = [], []
MOD = 1000000007
for i in range(n):
    a,b=map(int, input().split())
    x.append(a)
    k.append(b)
c,d,e,f = 1,1,1,1
for i in range(n):
    c=c*(k[i]+1)%MOD
    d = d*((pow(x[i],k[i]+1)-1)%MOD)//(x[i]-1)%MOD
    e = pow(e, k[i]+1,MOD)*pow(pow(x[i], k[i]*(k[i]+1)//2), f)%MOD
    f = f*(k[i]+1)%(MOD-1)
print(c,d,e)
