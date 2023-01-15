a = input()
b = input()
dp = [[int(1e9)]*(len(a)+1) for i in range(len(b)+1)]
dp[0][0]=0
for i in range(0, len(b)+1):
    for k in range(0, len(a)+1):
        if i:
            dp[i][k]=min(dp[i][k], dp[i-1][k]+1)
        if k:
            dp[i][k] = min(dp[i][k], dp[i][k-1]+1)
        if i and k:
            if b[i-1] != a[k-1]:
                dp[i][k] = min(dp[i][k], dp[i-1][k-1]+1)
            else:
                dp[i][k] = min(dp[i][k], dp[i-1][k-1])
#for i in dp: print(*i)
print(dp[-1][-1])
