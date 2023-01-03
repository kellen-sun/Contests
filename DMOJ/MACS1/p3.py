import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

while True:
    new=[]
    if len(array)==1:
        break
    for i in range(len(array)//3):
        new.append([array[3*i+2],array[3*i],array[3*i+1]])
    array=new[:]
array=array[0]
while not isinstance(array[0], int):
    array = [y for x in array for y in x]
print(*array)