import sys
from collections import deque
input = sys.stdin.readline



n,k = map(int, input().split())
votes = [input() for i in range(n)]
letters = list(votes[0])[:-1]
graph={i:set() for i in letters}
'''
for i in letters:
    for j in letters:
        if i!=j:
            s = True
            for a in votes:
                if not a.index(i)<a.index(j):
                    s=False
            if s:
                graph.setdefault(j,[]).append(i)'''
seen = set()
letters = set(letters)
for i in range(k):
    for j in range(n):
        seen.add(votes[j][i])
    left=letters-seen
    for j in seen:
        graph[j]=graph[j].union(left)

m=0

for i in graph.keys():
    queue = deque([(i,1)])
    while queue:
        current = queue.popleft()
        node = current[0]
        d = current[1]
        m=max(d,m)
        if graph.get(node)!=None:
            for i in graph[node]:
                queue.append((i,d+1))
print(m)
