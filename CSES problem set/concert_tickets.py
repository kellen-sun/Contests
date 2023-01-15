n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
c = [False]*n


def f(x):
    global c
    global i
    global a
    if a[x]>i or c[x]==True:
        return False
    else:
        return True
    
def search(start, end):
    global a
    while start<end:
        mid = start + (end - start + 1) // 2
        if f(mid):
            start=mid
        else:
            end = mid-1
    if f(start):
        c[start]=True
        return a[start]
    else:
        return -1

for i in b:
    print(search(0, n-1))
    
