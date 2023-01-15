n, m = map(int, input().split())
a = list(map(int, input().split()))
dp=[[0]*(m+1) for i in range(n)]
MOD = 1000000007
if a[0]==0:
    for i in range(len(dp[0])):
        dp[0][i]=1
else:
    dp[0][a[0]]=1
for i in range(1,n):
    if a[i]==0:
        for j in range(1,m+1):
            for k in [j-1,j,j+1]:
                if k>0 and k<=m:
                    dp[i][j] = (dp[i][j]+dp[i-1][k]) % MOD
    else:
        for k in [a[i]-1,a[i],a[i]+1]:
            if k>0 and k<=m:
                    dp[i][a[i]] = (dp[i][a[i]]+dp[i-1][k]) %MOD
            
print((sum(dp[-1])-dp[-1][0])%MOD)
#for i in dp: print(*i)
