import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

cases = int(input())
def solve(n,k,prefix):
    if k==0:
        print("0"*n)
        return
    if n==k:
        print(prefix+"1"*n)
        return
    if k==1:
        for i in range(n):
            string="0"*i + "1" + "0"*(n-1-i)
            print(prefix+string)
        return
    solve(n-1 ,k-1, prefix+"1")
    solve(n-1, k, prefix+"0")

for i in range(cases):
    n, k = map(int, input().split())
    print("The bit patterns are")
    solve(n,k,"")
    if i!=cases-1:
        print("")
