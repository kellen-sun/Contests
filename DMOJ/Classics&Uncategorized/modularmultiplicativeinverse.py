n, m = map(int, input().split())
MOD = m
x = [1, 0]
y = [0, 1]
q = []
while True:
    q.append(n//m)
    n, m = m, n%m
    if m==1:
        break
for i in q:
    x.append(x[-2]-x[-1]*i)
    y.append(y[-2]-y[-1]*i)
print(x[-1]%MOD)