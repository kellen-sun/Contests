a = int(input(''))
time = 0
friends = {}
times={}
for x in range(a):
    b = input('')
    if b[0] == 'R':
        if str(b[2:-1]) in friends:
            friends[str(b[2:-1])] = time
        else:
            friends[str(b[2:-1])] = time
            times[str(b[2:-1])] = 0
    elif b[0] == 'W':
        time = time + int(b[2])
    elif b[0] == 'S':
        times[str(b[2:-1])] = times[str(b[2:-1])] + time - friends[str(b[2:-1])]
    time = time+1
print(friends)
print(times)

