import sys
input = sys.stdin.readline
out=[]
t = int(input())
for ii in range(t):
    n,k,w = map(int, input().split())
    pins = [int(input()) for j in range(n)]
    sumpin = []
    sumpin.append(sum(pins[:w]))
    for j in range(1,n):
        if j+w-1<n:
            sumpin.append(sumpin[-1]-pins[j-1]+pins[j+w-1])
        else:
            sumpin.append(sumpin[-1]-pins[j-1])
    dp=[[0 for i in range(n)] for j in range(k+1)]
    for i in range(1,k+1):
        for j in range(n-1,-1,-1):
            if j==n-1:
                dp[i][j]=sumpin[-1]
            elif j+w>=n:
                dp[i][j]=max(sumpin[j], dp[i][j+1])
            else:
                dp[i][j]=max(dp[i][j+1], dp[i-1][j+w]+sumpin[j])
    out.append(dp[k][0])

for i in out: 
    print(i)