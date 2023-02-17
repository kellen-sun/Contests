n, m, r, c = map(int, input().split())
grid = [["z" for j in range(m)] for i in range(n)]

if r==1 and c==1:
    for i in range(m):
        grid[0][i]="a"
    for i in range(n):
        grid[i][0]="a"
    for i in grid:
        print(*i, sep="")
elif n==2 and m==2:
    if r==1 and c==2:
        print("IMPOSSIBLE")
    elif r==2 and c==1:
        print("IMPOSSIBLE")
    elif r==2 and c==2:
        print("aa")
        print("aa")
    elif r==0 and c==0:
        print("ab")
        print("ba")
    elif r==2 and c==0:
        print("aa")
        print("bb")
    elif r==0 and c==2:
        print("ab")
        print("ab")
    elif r==1 and c==1:
        print("aa")
        print("ab")
    elif r==1 and c==0:
        print("aa")
        print("bc")
    elif r==0 and c==1:
        print("ab")
        print("ac")
elif n==2:
    if r==0:
        if c!=m and c!=0:
            print(c*"a"+(m-c)*"b")
            print(c*"a"+(m-c)*"c")
        elif c==m:
            print("ab"+(m-2)*"c")
            print("ab"+(m-2)*"c")
        else:
            print("a"+(m-1)*"b")
            print("b"+(m-1)*"c")
    elif r==1:
        if c!=m and c!=0:
            print(m*"a")
            print(c*"a"+(m-c)*"b")
        elif c==0:
            print(m*"a")
            print("b"+(m-1)*"c")
        else:
            print("IMPOSSIBLE")
    else:
        if c%2==0:
            print(c//2*"a"+(m-c)*"b"+c//2*"a")
            print(c//2*"a"+(m-c)*"c"+c//2*"a")
        elif m%2==1:
            print((c-1)//2*"c" + (m-c)//2*"b" + "c" + (m-c)//2*"b" + (c-1)//2*"c")
            print((c-1)//2*"c" + (m-c)//2*"a" + "c" + (m-c)//2*"a" + (c-1)//2*"c")
        else:
            print("IMPOSSIBLE")
else:
    pass