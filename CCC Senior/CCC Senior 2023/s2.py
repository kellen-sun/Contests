import sys
input = sys.stdin.readline

n = int(input())
mountains = list(map(int, input().split()))

out = []

crops = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    start = 0
    for j in range(1+min(i, n-i-1)):
        start+=abs(mountains[i+j] - mountains[i-j])
        crops[i-j][i+j] = start
        crops[i+j][i-j] = start
    if i!=0:
        start = abs(mountains[i] - mountains[i-1])
        crops[i][i-1] = start
        crops[i-1][i] = start
        for j in range(min(i-1, n-i-1)):
            start += abs(mountains[i+j+1] - mountains[i-j-2])
            crops[i+j+1][i-j-2] = start
            crops[i-j-2][i+j+1] = start
            
for i in range(n):
    #i is query size
    m=10**10
    for j in range(n-i):
        m=min(m, crops[j][i+j])
    out.append(m)

print(*out)