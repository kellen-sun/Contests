import sys
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,m,k = map(int, input().split())
target = k-n
notes = [1]
current = 0
cur_note = 1
extra = 1
going_up = True
while target>=current:
    #forgot to consider m
    if len(notes)>n:
        break
    if target==current:
        for i in range(n-len(notes)):
            notes.append(cur_note)
        print(*notes)
        sys.exit()
    if target-current>=extra and cur_note<=m:
        if going_up:
            cur_note+=1
        else:
            cur_note-=1
        notes.append(cur_note)
        current+=extra
        extra+=1
    else:
        extra = 1
        going_up = not going_up

print(-1)