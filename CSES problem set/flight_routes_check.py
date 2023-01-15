n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
roads = {}
for i in a:
    if i[0] in roads.keys():
        roads[i[0]].append(i[1])
    else:
        roads[i[0]]=[i[1]]

