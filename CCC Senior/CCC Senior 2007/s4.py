n = int(input())
graph = {}
for i in range(1,n):
    graph[i]=[]
while True:
    m=list(map(int, input().split()))
    if m==[0,0]:
        break
    graph[m[0]].append(m[1])
dp = {n:1}
for i in range(n-1,0,-1):
    dp[i]=0
    for j in graph[i]:
        dp[i]+=dp[j]
print(dp[1])