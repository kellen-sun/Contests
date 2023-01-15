n = int(input())
low, high = 1, n*n
while low<high:
    mid, leq = (low+high)//2, 0
    for i in range(1,n+1): leq += min(n, mid//i)
    if leq>=(n*n+1)//2: high = mid
    else: low = mid+1
print(high)
