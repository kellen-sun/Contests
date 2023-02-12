import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
array = sorted([int(input()) for i in range(n)])
p1 = 0
p2 = 0
while len(array)>5:
    if array[-2]+array[-3]>array[-1]:
        longestside = array.pop(-1)
        secondside = array[-1]
        index = len(array)-1
        for i in range(len(array)-1,max(0, len(array)-5),-1):
            if array[i-1]+array[i-2]<=longestside:
                break
            secondside = array[i]
            index = i
        
        thirdside = array[index-1]
        index2 = index-1
        for i in range(index-1, max(-1, len(array)-6), -1):
            if secondside+array[i-1]<=longestside:
                break
            thirdside = array[i]
            index2 = i
        p1 = longestside+thirdside+secondside
        array.pop(index)
        array.pop(index2)
        break
    else:
        array.pop(-1)
while len(array)>2:
    if array[-2]+array[-3]>array[-1]:
        p2=array[-2]+array[-3]+array[-1]
        array.pop(-1)
        array.pop(-1)
        array.pop(-1)
        break
    else:
        array.pop(-1)

if p2==0 or p1==0:
    print(0)
else:
    print(p1+p2)