n, m, k = map(int, input().split())
array = [0]+list(map(int, input().split()))
differences = []
for i in range(1, len(array)):
    if array[i]<=m:
        differences.append(array[i]-array[i-1])
if k==0:
    print(max(0, max(differences)-1, m-sum(differences)))
else:
    maximum = 0
    for i in range(1, len(differences)):
        if differences[i]<=k or differences[i-1]<=k:
            maximum = max(maximum, differences[i]+differences[i-1])
        else:
            maximum = max(maximum, differences[i-1]+k)
            
    maximum = max(maximum, min(m-sum(differences[:-1])+1, differences[-1]+k))
    maximum = max(maximum, min(m-sum(differences)+k, m-sum(differences[:-1]))+1)
    print(maximum-1)