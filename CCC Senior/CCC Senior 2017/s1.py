n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
t=True
c,d=sum(a),sum(b)
for x in range(n-1,-1,-1):
    if c==d:
        print(x+1)
        t=False
        break
    else:
        c,d=c-a[x], d-b[x]
        #print(c,d)

if t:
    print(0)
