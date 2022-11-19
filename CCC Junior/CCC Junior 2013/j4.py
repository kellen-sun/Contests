t,c,l,summ, items = int(input()),int(input()),[],0,0
for i in range(c):
    l.append(int(input()))
while True:
    summ+=l.pop(l.index(min(l)))
    items+=1
    if summ>t:
        break
print(items-1)
