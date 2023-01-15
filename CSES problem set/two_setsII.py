n=int(input())
MOD = 1000000007
a = [i for i in range(1,n)]
tot = n*(n+1)//2

if tot%2==1:
    print(0)
else:
    tot=tot//2
    dp = [[0]*(tot+1) for i in range(n)]
    dp[0][0] = 1
    for i in range(1,n):
        for j in range(tot+1):
            dp[i][j] = dp[i-1][j]
            left = j-i
            if (left >= 0):
                dp[i][j] = (dp[i][j]+dp[i-1][left]) % MOD
            
    print(dp[-1][-1])
