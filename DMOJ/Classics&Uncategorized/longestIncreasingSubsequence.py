import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]
for i in range(1, n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        '''left, right = 0, len(dp)-1
        while left <= right:
            mid = (right+left)//2
            if dp[mid]>=arr[i]:
                right = mid-1
            else:
                left = mid+1'''
        idx = bisect_left(dp, arr[i])
        dp[idx]=arr[i]
print(len(dp))