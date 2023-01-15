w,h = map(int,input().split())
dp = [[0]*(w+1) for i in range(h+1)]
for i in range(h+1):
    for j in range(w+1):
        if i==j: dp[i][j]=0
        else:
            dp[i][j]=int(1e9)
            for k in range(i):
                dp[i][j] = min(dp[i][j], dp[k][j]+dp[i-k][j]+1)
            for k in range(j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[i][j-k]+1)
print(dp[-1][-1])
#for i in dp: print(*i)
