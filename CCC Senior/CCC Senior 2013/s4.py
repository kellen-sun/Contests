# seems impossible to get full points with python

n,m = map(int, input().split())
comparisons = []
for i in range(m):
    comparisons.append(list(map(int, input().split())))
compare = list(map(int, input().split()))

taller = []
graph = {}
for i in range(1,1+n):
    graph[i]=[]
for i in comparisons:
    graph[i[0]].append(i[1])

out = "unknown"
queue = [compare[0]]
queued = [True for i in range(n)]
while queue:
    current = queue.pop(0)
    if current == compare[1]:
        out = "yes"
        break
    for i in graph[current]:
        if queued[i-1]:
            queued[i-1]=False
            queue.append(i)
queue = [compare[1]]
queued = [True for i in range(n)]
if out!="yes":
    while queue:
        current = queue.pop(0)
        if current == compare[0]:
            out = "no"
            break
        for i in graph[current]:
            if queued[i-1]:
                queued[i-1]=False
                queue.append(i)
print(out)