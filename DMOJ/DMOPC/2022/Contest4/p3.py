t = int(input())
for testcase in range(t):
    x,y,k = map(int, input().split())
    if x==y:
        print(2* (x//(k+1)))
        continue
    if y>x:
        x,y = y,x
    #now x>y without changing our answer
    c=x//k
    x=x%k
    y=y-x//k
    if y<0: y==y%2
    if y//k+1<=x:
        c+=y//k+1
    else:
        c+=y//k
        y=y%k
        x=x-y//k
        c+=2
    print(c)
