y=str(int(input())+1)
while True:
    t,v,a=int(y),list(y),True
    for x in range(len(v)):
        b=v.pop(x)
        if b in v:
            a=False
        v.insert(x,b)
    if a:
        print(y)
        break
    y=str(t+1)
