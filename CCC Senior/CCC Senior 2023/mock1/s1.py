import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

ifib = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]
fib = [str(i) for i in ifib]
t = int(input())
def check(N):
    global fib
    for i in fib:
        if int(i)==int(N):
            return True
        if i==N[:len(i)]:
            if check(N[len(i):]):
                return True
    return False

out = []
for i in range(t):
    n=input()
    if int(n)==13 or int(n)==21 or int(n)==55 or int(n)==233:
        out.append(True)
    else: out.append(check(n) and (int(n) not in ifib))
for i in out:
    if i:
        print("YES")
    else: print("NO")