#basically change the grid into a graph and then count how many connected components there are
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
grid = [input() for i in range(n)]

def init_queued():
    global n
    global m
    queued = {}
    for i in range(n):
        for j in range(m):
            queued[(i,j)]=False
    return queued

in_component = init_queued()
components = 0
for i in range(n):
    for j in range(m):
        if not in_component[(i,j)]:
            components+=1
            queue = deque([(i,j)])
            #queued = init_queued()
            while queue:
                current = queue.popleft()
                cur_value = grid[current[0]][current[1]]
                if cur_value=="S":
                    if not in_component[(current[0]+1, current[1])]:
                        #queued[(current[0]-1, current[1])] = True
                        queue.append((current[0]+1, current[1]))
                        in_component[(current[0]+1, current[1])]=True
                if cur_value=="N":
                    if not in_component[(current[0]-1, current[1])]:
                        #queued[(current[0]-1, current[1])] = True
                        queue.append((current[0]-1, current[1]))
                        in_component[(current[0]-1, current[1])]=True
                if cur_value=="W":
                    if not in_component[(current[0], current[1]-1)]:
                        #queued[(current[0]-1, current[1])] = True
                        queue.append((current[0], current[1]-1))
                        in_component[(current[0], current[1]-1)]=True
                if cur_value=="E":
                    if not in_component[(current[0], current[1]+1)]:
                        #queued[(current[0]-1, current[1])] = True
                        queue.append((current[0], current[1]+1))
                        in_component[(current[0], current[1]+1)]=True
            #issue is that right now might not be starting on first node kinda of the component, should prolly make it so that edges are bidirectional so bfs search backwards and forwards.
print(components)

