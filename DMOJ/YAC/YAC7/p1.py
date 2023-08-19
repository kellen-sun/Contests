import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
out = []
#odd first, then all evens then remaining odds
#pieces earlier in the manuscript outputted first BRUHH
odds = deque([])
evens = deque([])

for i in range(len(array)):
    if array[i]%2:
        odds.append(i+1)
    else:
        evens.append(1+i)

if len(odds)==0:
    #no odds
    print(sum(array)//2)
    print(*[i for i in range(1, len(array)+1)])
    sys.exit()

out.append(odds.popleft())

while True:
    if odds and evens:
        if len(odds)>1:
            if odds[0]<evens[0]:
                out.append(odds.popleft())
                out.append(odds.popleft())
            else:
                out.append(evens.popleft())
        else:
            out = out+list(evens)
            out.append(odds[0])
            break
    elif odds:
        out = out+list(odds)
        break
    elif evens:
        out = out+list(evens)
        break
    else:
        break

num = 0
for i in range(len(out)):
    cur = array[out[i]-1]
    if cur%2==0:
        num+=cur//2 -1
    else: num+=cur//2
print(int(num))
print(*out)