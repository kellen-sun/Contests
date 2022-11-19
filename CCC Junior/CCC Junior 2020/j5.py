m = int(input())
n = int(input())
c = []
#Creating the 2-D array
for x in range(m):
    b = input()
    a = b.split()
    c.append(a)
queue=[(0,0)]
retur='no'
while queue:
    node=queue.pop(0)
    value=int(c[node[0]][node[1]])
    if node==(m-1, n-1):
        retur = 'yes'
        break
    for x in range(1,m+1):
        if value%x==0:
            if value//x<=n:
                queue.append((int(x)-1, int(int(c[node[0]][node[1]])//x)-1))
print(retur)



