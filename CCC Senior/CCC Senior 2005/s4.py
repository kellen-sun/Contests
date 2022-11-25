n=int(input())
for x in range(n):
    L = int(input())
    zombies = []
    for i in range(L):
        zombies.append(input())
    zombies.insert(0, zombies[-1])
    m=0
    seen = []
    current = 0
    for i in range(L+1):
        if zombies[i] not in seen:
            seen.append(zombies[i])
            current+=1
        else:
            current-=1
            seen.pop(-1)
        m=max(m, current)
    print(L*10-20*(m-1))