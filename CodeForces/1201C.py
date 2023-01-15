size, maxOps = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def f(x):
    opsNeeded = 0
    for i in range((size - 1) // 2, size):
        opsNeeded += max(0, x - arr[i])
    return opsNeeded <= maxOps

def lastTrue(lo, hi):
	lo -= 1
	while lo < hi:
		mid = lo + (hi - lo + 1) // 2;
		if f(mid):
			lo = mid
		else:
			hi = mid - 1
	return lo

print(lastTrue(1, int(2e9)))
