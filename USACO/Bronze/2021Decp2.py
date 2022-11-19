n=int(input())
end = list(map(int, input().split()))
start = list(map(int, input().split()))
p1, p2=0,n-1
c=0
def change(p1, p2, c, v):
    for i in range(p1,p2+1):
        c[i]=c[i]+v
    return c
while start!=end:
    changed=True
    if start[p1]==end[p1]:
        p1+=1
        #print("A")
    elif start[p2]==end[p2]:
        p2-=1
        #print("A")
    if start[p1]>end[p1] and start[p2]>end[p2]:
        start = change(p1, p2, start, -1)
        c+=1
        #print(start)
    elif start[p1]<end[p1] and start[p2]<end[p2]:
        c+=1
        start = change(p1, p2, start, 1)
        #print(start)
    else:
        p2-=1
        #changed=False
    if p1==p2 and changed:
        p2=n-1
        #print(changed)
    if p1+1==p2:
        if (start[p1]<end[p1] and start[p2]>end[p2]):
            c+=1
            start[p2]-=1
        elif (start[p1]>end[p1] and start[p2]<end[p2]):
            start[p2]+=1
            c+=1
        
print(c)
