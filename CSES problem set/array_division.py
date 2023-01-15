n, k = map(int, input().split())
a = list(map(int, input().split()))

def f(x):
    global a
    global n
    global k
    c=0
    ans=1
    for i in a:
        if i>x:
            ans=float('inf')
            break
        elif i+c>x:
            ans+=1
            c=i
        else:
            c+=i
    #print(ans)
    if ans>k:
        return False
    else:
        return True
def search(start, end):
    while start<end:
        mid = start + (end - start+1) // 2
        #print(mid)
        if not f(mid):
            start=mid
        else:
            end = mid-1
    return start
#print(f(7))
print(search(0, int(2e18))+1)
