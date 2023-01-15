x, n = map(int, input().split())
a = list(map(int, input().split()))
MOD = 1000000007
c = [0]*2100000
c[0]=1
for i in range(n):
    for x in a:
        c[i+x]=(c[i+x]+c[i])%MOD
print(c[n])
