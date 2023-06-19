import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

lookup = [
    [1], 
    [1,-1], 
    [1,-2,1],
    [1,-4,-4,8],
    [2,-13,12,-11,10],
    [1,-2,1,-1,1,-1],
    [11,-13,12,-11,10,-9,8],
    [11,-13,12,-11,10,-9,8,-7]
    ]
if n<9:
    print(*lookup[n-1])

else:
    l=[]
    if n%2==1:
        for i in range(8,8+n-1):
            l.append((-1)**i * i)
        if (n+1)//2 %2==0:
            l.append(((n+1)//2) * 2 -((n+1)//2) //2 + 5)
        else:
            l.append((n+1)//2 * 2 -((n+1)//2+1) //2 + 6)
    else:
        l.append(-7)
        for i in range(8,8+n-2):
            l.append((-1)**i * i)
        if (n+1)//2 %2==0:
            l.append(((n+1)//2) * 2 -((n+1)//2) //2 + 5)
        else: 
            l.append(((n+1)//2) * 2 -((n+1)//2 +1) //2 + 6)
    print(*l)
