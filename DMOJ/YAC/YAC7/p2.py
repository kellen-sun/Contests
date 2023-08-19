import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

t = int(input())
for iii in range(t):
    n, m = map(int, input().split())
    if n==m:
        if n%2 == 0:
            out = [[-1 for i in range(n)] for j in range(n)]
            out[0][0] = 1
            cur = 2
            for i in range(n):
                if i%2==0:
                    #even means going down
                    for j in range(1, n):
                        out[i][j] = cur
                        cur+=1
                else:
                    for j in range(n-1, 0, -1):
                        out[i][j] = cur
                        cur+=1
            for i in range(n-1, 0, -1):
                out[i][0] = cur
                cur+=1
            for i in out:
                print(*i)
        else:
            if n == 1:
                print(-1)
            else:
                out = [[-1 for i in range(n)] for j in range(n)]
                cur = 1
                for i in range(n-1):
                    if i%2 == 0:
                        out[i][0] = cur
                        cur+=1
                        out[i][1] = cur
                        cur+=1
                    else:
                        out[i][1] = cur
                        cur+=1
                        out[i][0] = cur
                        cur+=1
                for i in range(n):
                    out[-1][i] = cur
                    cur+=1
                for j in range(n-1, 1, -1):
                    if j%2==0:
                        #j odd means going up
                        for i in range(n-2, -1, -1):
                            out[i][j] = cur
                            cur+=1
                    else:
                        for i in range(n-1):
                            out[i][j] = cur
                            cur+=1
                for i in out:
                    print(*i)
    #now we have n!=m, most difficult of which is n and m both odd
    #to do evens we can still loop
    elif n==1 or m==1:
        print(-1)
    elif n==2:
        cur = 1
        out = [[-1 for i in range(m)] for j in range(n)]
        for i in range(m):
            out[0][i] = cur
            cur+=1
        for i in range(m):
            out[1][m-1-i] = cur
            cur+=1
        for i in out:
            print(*i)
    elif m==2:
        cur = 1
        out = [[-1 for i in range(m)] for j in range(n)]
        for i in range(n):
            out[i][0] = cur
            cur+=1
        for i in range(n):
            out[n-1-i][1] = cur
            cur+=1
        for i in out: print(*i)
    elif n%2==0:
        cur = 1
        out = [[-1 for i in range(m)] for j in range(n)]
        for i in range(n):
            out[i][0] = cur
            cur+=1
        for i in range(n-1, -1, -1):
            if i%2==0:
                for j in range(m-1, 0,-1):
                    out[i][j]=cur
                    cur+=1
            else:
                for j in range(1, m):
                    out[i][j] = cur
                    cur+=1
        for i in out: print(*i)
    elif m%2==0:
        cur = 1
        out = [[-1 for i in range(m)] for j in range(n)]
        out[0][0] = cur
        cur+=1
        for j in range(m):
            if j%2 == 0:
                #goes down
                for i in range(1, n):
                    out[i][j] = cur
                    cur+=1
            else:
                for i in range(n-1, 0, -1):
                    out[i][j] = cur
                    cur+=1
        for j in range(m-1, 0, -1):
            out[0][j] = cur
            cur+=1
        for i in out: print(*i)
    else:
        #both odd can still do the swiggle thing
        cur = 1
        out = [[-1 for i in range(m)] for j in range(n)]
        for i in range(n-1):
            if i%2 == 0:
                out[i][0] = cur
                cur+=1
                out[i][1] = cur
                cur+=1
            else:
                out[i][1] = cur
                cur+=1
                out[i][0] = cur
                cur+=1
        for j in range(m):
            out[-1][j] = cur
            cur+=1
        for j in range(m-1, 1, -1):
            if j%2 == 0:
                for i in range(n-2, -1, -1):
                    out[i][j] = cur
                    cur+=1
            else:
                for i in range(n-1):
                    out[i][j] = cur
                    cur+=1
        for i in out: print(*i)