n, k = map(int, input().split())
a = list(map(int, input().split()))
b=sorted(a)
m = b[0]

for i in range(1, k):
    if b[i]-b[i-1]>m:
        m=b[i]-b[i-1]
if n-b[-1]>m:
    m=n-b[-1]
out = [m]

'''
for i in a[::-1][:-1]:
    l=b.index(i)
    b.pop(l)
    #print(b, l)
    if l == len(b)-1:
        if n-b[-1]>m:
            m=n-b[-1]
    elif l==0:
        if b[0]>m:
            m=b[0]
    elif len(b)==1:
        
        if b[0]>m:
            
            m=b[0]
        elif n-b[0]>m:
            #print("HHHHH")
            m=n-b[0]
    else:
        if b[l+1]-b[l]>m:
            m=b[l+1]-b[l]
    

    out.append(m)
'''

b.append(n)
b.insert(0, 0)
for i in a[::-1][:-1]:
    l=b.index(i)
    b.pop(l)
    if (b[l]-b[l-1])>m:
        m=b[l]-b[l-1]
    out.append(m)
print(*out[::-1])
