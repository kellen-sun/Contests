n,m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
T = [list(map(int, input().split())) for i in range(n)]
if A==T:
    print("YES")
else:
    if sum([sum(i) for i in A])-sum([sum(i) for i in T])%2==0:
        print("YES")
    else:
        print("NO")