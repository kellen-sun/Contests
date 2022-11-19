path=[(0, -1), (0, -2), (0, -3), (1, -3), (2, -3), (3, -3), (3, -4), (3, -5), (4, -5), 
(5, -5), (5, -4), (5, -3), (6, -3), (7, -3), (7, -4), (7, -5), (7, -6), (7, -7),
(6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7), (0, -7), (-1, -7), (-1, -6), (-1, -5)]

trigger=False
while True:
    x=input('')
    if x[0]=='d':
        for y in range(int(x[1:])):
            a=(path[-1][0], path[-1][1]-1)
            if a in path:
                trigger=True
            path.append(a)
    elif x[0]=='u':
        for y in range(int(x[1:])):
            a=(path[-1][0], path[-1][1]+1)
            if a in path:
                trigger=True
            path.append(a)
    elif x[0]=='r':
        for y in range(int(x[1:])):
            a=(path[-1][0]+1, path[-1][1])
            if a in path:
                trigger=True
            path.append(a)
    elif x[0]=='l':
        for y in range(int(x[1:])):
            a=(path[-1][0]-1, path[-1][1])
            if a in path:
                trigger=True
            path.append(a)
    elif x[0]=='q':
        break
    print(path[-1])
    if trigger:
        print('Danger')
        break
    else:
        print('safe')
