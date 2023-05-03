t = int(input())
out = []


for testcase in range(t):
    n, k = map(int, input().split())
    perms = list(map(int, input().split()))
    if k==0:
        c=0
        currentlarges = 0
        for i in perms:
            if i<currentlarges:
                c+=1
            else:
                currentlarges=i
        out.append(c)
        if c>0:
            out.append(" ".join(list(map(str, range(c, 0, -1)))))

for i in out:
    print(i)