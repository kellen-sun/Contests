import sys
sys.setrecursionlimit(200006)

n = int(input())
a = list(map(int, input().split()))
t = {}
for i in range(n-1):
    if a[i] in t.keys():
        t[a[i]].append(i+2)
    else:
        t[a[i]] = [i+2]
#print(t)
e = {}
def count(n):
    global t
    global e
    if n not in t.keys():
        e[n]=0
        return 0
    else:
        e[n]=0
        for i in t[n]:
            e[n]=count(i)+e[n]+1
        return e[n]
count(1)
#print(e)
for i in sorted(list(e.keys())):
    print(e[i], end=" ")
