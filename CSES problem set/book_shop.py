n, x = map(int, input().split())
prices = [0]+list(map(int, input().split()))
pages = [0]+list(map(int, input().split()))
dp = [[0]*(x+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,x+1):
        if j>=prices[i]:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-prices[i]]+pages[i], dp[i][j-1])
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
