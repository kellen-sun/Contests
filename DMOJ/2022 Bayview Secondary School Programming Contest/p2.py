import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
out = []
def check(a,b):
    if a[-1]=="7":
        if len(a)>1:
            if a[-2]!="1":
                if len(b)>1:
                    if b[-2:]=="11":
                        return True
        else:
            if len(b)>1:
                if b[-2:]=="11":
                    return True
    return False
for i in range(n):
    a,b = input().split()
    if check(a,b) or check(b,a):
        out.append("YES")
    else:
        out.append("NO")
for i in out:
    print(i)
    