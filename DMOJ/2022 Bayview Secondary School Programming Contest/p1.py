n = int(input())
out = []
cur = 0
for i in range(n):
    cur+=int(input())
    out.append(cur)

for i in out: print(i)