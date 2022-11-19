a = int(input(''))
l ={}
j = {}
k = 0
for x in range(a):
    d = []
    t = []
    v = 0
    b = input('')
    while v < len(b):
        g = b[v]
        if v+1 == len(b):
            if g != b[-1]:
                d.append(1)
                t.append(g)
                v = v+1
            else:
                y = v
                while v < len(b) and g == b[v]:
                    v=v+1
                d.append(v-y)
                t.append(b[v-1])
        else:
            if g != b[v+1]:
                d.append(1)
                t.append(g)
                v = v+1
            else:
                y = v
                while v < len(b) and g == b[v]:
                    v=v+1
                d.append(v-y)
                t.append(b[v-1])
    l[x] = t
    j[x] = d

for key, value in l.items():
    print(end = '\n')
    for f in range(len(value)):
        print(str(j[key][f]) + ' ' + str(value[f]), end = ' ')

