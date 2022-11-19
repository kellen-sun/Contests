a = int(input(''))
time = 0
friends = {}
times={}
for x in range(a):
    b = input()
    if b[0] == 'R':
        if str(b[2:]) in friends:
            friends[str(b[2:])] = time
        else:
            friends[str(b[2:])] = time
            times[str(b[2:])] = 0
        time+=1
    elif b[0] == 'W':
        time = time + int(b[2:])
    elif b[0] == 'S':
        times[str(b[2:])] = times[str(b[2:])] + time - friends[str(b[2:])]-1
        time += 1
for i in sorted(friends.keys()):
    if times[i]!=0:
        print(i, times[i])
    else:
        print(i, "-1")