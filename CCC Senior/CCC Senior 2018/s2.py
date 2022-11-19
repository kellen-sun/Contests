n=int(input())
table=[]
for x in range(n):
    table.append(list(map(int,input().split())))
#print(list(zip(*table[::-1])))
for x in range(4):
    a=True
    for y in range(2):
        tt=list(zip(*table[::-1]))
        for z in range(n):
            if list(table[z])!=list(sorted(table[z])) and y==0:
                a=False
                break
            elif list(tt[z])!=list(sorted(tt[z], reverse=True)) and y==1:
                a=False
                break
    if a:
        break
        
    table=list(zip(*table[::-1]))
for x in table:
    print(*x)
