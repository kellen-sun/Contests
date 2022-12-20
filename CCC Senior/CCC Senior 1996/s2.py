import sys
import heapq
input = sys.stdin.readline
out = []
n = int(input())
for i in range(n):
    out.append("")
    k = input()[:-1]
    kk=k
    out.append(k)
    while len(k)>2:
        last = k[-1]
        k=k[:-1]
        k=str(int(k)-int(last))
        out.append(k)
    if int(k)%11==0:
        out.append("The number "+ kk+ " is divisible by 11.")
    else:
        out.append("The number "+ kk+ " is not divisible by 11.")
for i in out[1:]: print(i)