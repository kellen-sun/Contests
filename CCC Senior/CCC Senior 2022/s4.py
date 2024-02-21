n,c=map(int, input().split())
p=list(map(int, input().split()))
points = [0 for i in range(c)]
for i in p:
    points[i] += 1
#print(points)
sol=0
circle = points + points
pre = []
s = sum(circle[:c//2+1])
for i in range(c):
    pre.append(s)
    s -= circle[i]
    s += circle[i+c//2+1]
#print(pre)
x = 0
for i in range(c):
    x += (pre[i]-points[i])*(pre[i]-points[i]-1)*points[i]//2 + (pre[i]-points[i])*points[i]*(points[i]-1)//2 + points[i]*(points[i]-1)*(points[i]-2)//6
sol = n*(n-1)*(n-2)//6 - x
if c%2 == 0:
    toaddback = 0
    for i in range(c):
        A = circle[i]
        B = circle[c//2+i]
        toaddback += A*(A-1)*B + A*B*(B-1)
    sol += toaddback//4
print(sol)
