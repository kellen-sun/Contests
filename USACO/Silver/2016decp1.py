import sys

def atMost(x):
    global arr
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo

sys.stdin = open("haybales.in", "r")
sys.stdout = open("haybales.out", "w")

n,q = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in range(q):
    start,end = map(int, input().split())
    print(atMost(end)-atMost(start-1))
