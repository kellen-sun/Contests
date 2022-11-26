graph={
    1:[6],
    2:[6],
    3:[4,5,6,15],
    4:[3,5,6],
    5:[3,4,6],
    6:[1,2,3,4,5,7],
    7:[6,8],
    8:[7,9],
    9:[8,10,12],
    10:[9,11],
    11:[10,12],
    12:[9,11,13],
    13:[12,14,15],
    14:[13],
    15:[3,13],
    16:[17,18],
    17:[16,18],
    18:[16,17]
}

def i(x,y):
    global graph
    if x in graph.keys():
        graph[x].append(y)
    else:
        graph[x]=[y]
    if y in graph.keys():
        graph[y].append(x)
    else:
        graph[y]=[x]

def d(x,y):
    global graph
    graph[x].remove(y)
    graph[y].remove(x)

def n(x):
    return len(graph[x])

def f(x):
    global graph
    ff = []
    for i in graph[x]:
        for j in graph[i]:
            ff.append(j)
    ff=list(set(ff))
    for i in graph[x]:
        if i in ff:
            ff.remove(i)
    if x in ff:
        ff.remove(x)
    return len(ff)

def s(x,y):
    global graph
    queue = [[x,0]]
    queued = [x]
    while queue:
        cur = queue.pop(0)
        if cur[0] == y:
            return cur[1]
        for i in graph[cur[0]]:
            if i not in queued:
                queued.append(i)
                queue.append([i, cur[1]+1])
    return "Not connected"

out=[]
while True:
    task = input()
    if task == "q": 
        break
    elif task == "i":
        x=int(input())
        y=int(input())
        i(x,y)
    elif task == "d":
        x=int(input())
        y=int(input())
        d(x,y)
    elif task == "n":
        x=int(input())
        out.append(n(x))
    elif task == "f":
        x=int(input())
        out.append(f(x))
    elif task == "s":
        x=int(input())
        y=int(input())
        out.append(s(x,y))

for i in out:
    print(i)