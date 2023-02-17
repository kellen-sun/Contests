import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
river = [int(input()) for i in range(n)]
r = dict(Counter(river))

m = 0
tbc = []
m2 = 0
tbc2 = []
for key in r.keys():
    if r[key]>m:
        m=r[key]
        tbc2 = tbc.copy()
        tbc = [key]
    elif r[key]==m:
        tbc.append(key)
    elif r[key]>m2:
        m2 = r[key]
        tbc2 = [key]
    elif r[key]==m2:
        tbc2.append(key)

if len(tbc)==1:
    print(max(abs(tbc[0]-max(tbc2)), abs(tbc[0]-min(tbc2))))
else:
    print(max(tbc)-min(tbc))