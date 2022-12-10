import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph={}
for i in range(n):
    a=input()
    b=a[-2]
    a=a[0]
    if graph.get(a)!=None:
        graph[a].append(b)
    else:
        graph[a]=[b]
    if b.upper()==b and graph.get(b)==None:
        graph[b]=[]
#print(graph)
for i in range(65,91):
    letter = chr(i)
    if graph.get(letter)!=None:
        add = []
        queue = [letter]
        queued = [letter]
        while queue:
            current = queue.pop()
            if current.lower()==current:
                add.append(current)
            else:
                for i in graph[current]:
                    if i not in queued:
                        queued.append(i)
                        queue.append(i)
        print(letter+" = {", end="")
        print(*sorted(add), sep=",", end = "")
        print("}")