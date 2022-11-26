n=int(input())
friends = {}
for i in range(n):
    m=list(map(int, input().split()))
    friends[m[0]]=m[1]


out = []
while True:
    task = list(map(int, input().split()))
    if task == [0,0]:
        break
    dist = 0
    cur = task[0]
    while True:
        cur = friends[cur]
        if cur==task[1]:
            out.append("Yes "+str(dist))
            break
        elif cur==task[0]:
            out.append("No")
            break
        
        dist+=1
for i in out:
    print(i)