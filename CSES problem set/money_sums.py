n = int(input())
x = list(map(int, input().split()))
dp = [[False]*(1000*n+1) for i in range(n+1)]
dp[0][0]=True
for i in range(1,n+1):
    for j in range(len(dp[i])):
        dp[i][j]=dp[i-1][j]
        left = j-x[i-1]
        if dp[i-1][left] and left>=0:
            dp[i][j]=True
possible =[]
for i in range(1, 1000*n+1):
    if dp[n][i]:
        possible.append(i)
print(len(possible))
print(*possible)
