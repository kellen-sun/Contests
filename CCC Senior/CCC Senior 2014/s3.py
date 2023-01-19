import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

t = int(input())
out = []

def test(array):
    lake = 1
    #mountain = deque(array)
    branch = deque()
    for i in array:
        if i==lake:
            lake+=1
        else:
            branch.append(i)
        for j in range(len(branch)):
            if branch[-1]==lake:
                lake+=1
                branch.pop()
            else:
                break
    if branch:
        return "N"
    else:
        return "Y"
        

for testcase in range(t):
    n = int(input())
    array = [int(input()) for i in range(n)]
    out.append(test(array[::-1]))

for i in out: print(i)