import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

h = int(input())
a = int(input())
s = int(input())

print(max(0,min(h,a)-s))