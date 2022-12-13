import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
members = []
for i in range(n):
    members.append(list(map(int, input().split())))

members=sorted(members, key=lambda x:x[0], reverse=True)

c=-float('inf')
currentmmin = [members[i][1] for i in range(m)]
for i in range(m-1,len(members)):
    currentmmin.append(members[i][1])
    mmm = max(currentmmin)
    currentmmin.remove(mmm)
    d = members[i][0]-max(currentmmin)
    c=max(d,c)
print(c)