R, C = map(int, input().split())
room = [input() for i in range(R)]

preprocess = []
for i in range(R):
    toadd = [0]
    for j in range(C):
        if room[i][j]=="X":
            toadd.append(toadd[-1]+1)
        else:
            toadd.append(toadd[-1])
    preprocess.append(toadd)

currmax = 0
for i in range(C+1):
    for j in range(i+1, C+1):
        m = 0
        lastwork = 0
        for k in range(R):
            if preprocess[k][i]==preprocess[k][j]:
                lastwork+=1
                m = max(m, lastwork)
            else:
                lastwork = 0
        if m!=0:
            currmax = max(2*(j-i+m), currmax)

print(max(0, currmax-1))