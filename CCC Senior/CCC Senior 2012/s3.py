import sys
import heapq
input = sys.stdin.readline
from collections import Counter

n = int(input())
array = [int(input()) for i in range(n)]
counted = dict(Counter(array))
reverse = {}
for i in counted.keys():
    reverse.setdefault(counted[i],[]).append(i)
if len(reverse[max(reverse.keys())])>1:
    using = reverse[max(reverse.keys())]
    print(max(using)-min(using))
else:
    m = reverse[max(reverse.keys())][0]
    reverse.pop(max(reverse.keys()))
    using = reverse[max(reverse.keys())]
    print(max(abs(m-min(using)),abs(m-max(using))))