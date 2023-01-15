def calculate(a,b):
    if a<b:
        a,b=b,a
    if a > 2 * b:
        return("NO")
    elif (a + b) % 3 == 0:
        return("YES")
    else:
        return 'NO'

n=int(input())
out=[]
for x in range(n):
    inp=list(map(int, input().split()))
    a,b=inp[0],inp[1]
    out.append(calculate(a,b))
for x in out:
    print(x)
