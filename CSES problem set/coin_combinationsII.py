x, n = map(int, input().split())
a = list(map(int, input().split()))
MOD = 1000000007
dp = [[0 for i in range(n+1)] for j in range(x+1)]
for i in range(1,x+1):
    for j in range(1,1+n):
        if j-a[i-1]>0:
            dp[i][j]=(dp[i-1][j]+dp[i][j-a[i-1]])%MOD
        else:
            dp[i][j]=dp[i-1][j]
        if a[i-1]==j:
            dp[i][j] = (dp[i][j]+1)%MOD
        
print(dp[x][j])
