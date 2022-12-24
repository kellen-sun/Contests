import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
k = int(input())

strokes = [input().split() for i in range(k)]
r = [0 for i in range(m)]
c = [0 for i in range(n)]
for i in strokes:
    num = int(i[1])
    if i[0]=="R":
        r[num-1]=1- r[num-1]
    else:
        c[num-1]=1- c[num-1]
sr = sum(r)
sc = sum(c)
print(sr*n+sc*m-2*sc*sr)