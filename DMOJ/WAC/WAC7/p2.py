t = int(input())
out = []
for i in range(t):
    a,b = map(int, input().split())
    out.append(a+b-1)
for i in out:
    print(i)