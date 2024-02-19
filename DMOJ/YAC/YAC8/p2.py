import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))
have = Counter(arr)
wants = []
done = True
for i in arr:
    if have[x ^ i] != 0:
        if x ^ i != i:
            print("YES")
            done = False
            break
        else:
            if have[x^i] !=1:
                print("YES")
                done = False
                break
if done:
    print("NO")