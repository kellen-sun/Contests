import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lights = [int(input())==1 for i in range(n)]

queue = deque([(lights, 0)])
# no queued?
def next(lights):
    cc = 0
    for i in range(len(lights)):
        if lights[i]:
            cc+=1
        else: cc=0
        if cc==4:
            lights[i]=False
            lights[i-1]=False
            lights[i-2]=False
            lights[i-3]=False
        if cc>4:
            lights[i]=False
    return lights

while queue:
    current = queue.popleft()
    arr = current[0]
    count = current[1]
    if arr == [False for i in range(n)]:
        print(count)
        break
    for i in range(n):
        if arr[i]==False:
            a=arr.copy()
            a[i]=True
            queue.append([next(a),count+1])