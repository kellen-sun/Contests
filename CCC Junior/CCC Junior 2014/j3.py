a, d = 100, 100
for x in range(int(input())):
    v=input()
    b, c = int(v[0]), int(v[2])
    if b>c:
        d-=b
    elif c>b:
        a-=c
print(str(a)+'\n'+str(d))
