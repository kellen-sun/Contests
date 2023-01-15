n = int(input())
a = list(map(int, input().split()))
dp = [[0]*n for i in range(n)]
for i in range(n-1,-1,-1):
    for j in range(n):
        if j>=i:
            if i==j:
                dp[i][j]=a[i]
            else:
                dp[i][j]=max(a[i]-dp[i+1][j], a[j]-dp[i][j-1])
print((sum(a)+dp[0][-1])//2)
