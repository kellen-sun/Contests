import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

if n < 1001:
    paths = list(map(int, input().split()))
    ores = [list(map(int, input().split()[1:])) for i in range(n)]
    ores_counter = [Counter(ores[i]) for i in range(n)]

    fullgraph = [[] for i in range(n+1)]
    for i in range(n):
        fullgraph[i+1].append(paths[i])
        fullgraph[paths[i]].append(i+1)
    #print(fullgraph)
    for i in range(n):
        # remove each node
        fullgraph[i+1].remove(paths[i])
        fullgraph[paths[i]].remove(i+1)

        # traverse starting from cell i+1
        queue = deque([i+1])
        seen = [0 for i in range(n+1)]
        seen[i+1] = 1
        while queue:
            cur = queue.pop()
            for j in fullgraph[cur]:
                if not seen[j]:
                    queue.append(j)
                    seen[j] = 1
        #print(seen)
        newcount = Counter([])
        for j in range(1, len(seen)):
            if seen[j]:
                newcount = newcount + ores_counter[j-1]
        totals = sorted([j[1] for j in newcount.items()], reverse=True)
        m = 0
        for j in range(len(totals)):
            m = max(m, (j+1)*totals[j])
        print(m)

        # add it back in
        fullgraph[i+1].append(paths[i])
        fullgraph[paths[i]].append(i+1)

else:
    paths = list(map(int, input().split()))
    ores = [list(map(int, input().split()[1:])) for i in range(n)]
    ores_counter = [Counter(ores[i]) for i in range(n)]
    suffixsum = [0 for i in range(n)]
    s = Counter([])
    for i in range(n-1, -1, -1):
        s = s + ores_counter[i]
        suffixsum[i] = s
    for i in range(n):
        totals = sorted([j[1] for j in suffixsum[i].items()], reverse=True)
        m = 0
        for j in range(len(totals)):
            m = max(m, (j+1)*totals[j])
        print(m)