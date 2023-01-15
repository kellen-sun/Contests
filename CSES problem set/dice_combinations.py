n = int(input())
MOD = 1000000007
c = [0]*1000010
c[0]=1
for i in range(n):
    for x in range(1,7):
        c[i+x]=(c[i+x]+c[i])%MOD
print(c[n])
