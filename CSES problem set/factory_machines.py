n, t = map(int, input().split())
arr = list(map(int, input().split()))

def f(m):
    global arr
    global t
    c=0
    for i in arr:
        c+=m//i
    if c>=t:
        return True
    else: return False

def search(start, end):
    while start<end:
        mid = start + (end - start + 1) // 2
        #print(mid)
        if not f(mid):
            start=mid
        else:
            end = mid-1
    return start

print(search(1, int(2e20))+1)
