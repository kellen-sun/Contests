import sys
input = sys.stdin.readline

n,m = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(m)]

def dfs(current, graph, queued):
    global n
    if current == n:
        return True
    for i in graph[current]:
        if not queued[i]:
            queued[i]=True
            if dfs(i, graph, queued):
                return True
    return False

for i in range(m):
    e=edges.copy()
    e.pop(i)
    g=[[] for i in range(n+1)]
    for j in e:
        g[j[0]].append(j[1])

    if dfs(1,g,[False for i in range(n+1)]):
        print("YES")
    else:
        print("NO")
