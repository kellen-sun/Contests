n=int(input())
a=list(map(int, input().split()))
towers=[[a[0]]]

def search(t,val,p1,p2):
    if len(t)>1:
        if t[-1][-1]<=val:
            t.append([val])
            return t
        if (p1+p2)//2==0 and t[0][-1]>val:
            t[(p1+p2)//2].append(val)
            return t
        if (t[(p1+p2)//2][-1]<=val and t[(p1+p2)//2+1][-1]>val):
            t[(p1+p2)//2+1].append(val)
            return t
        elif t[(p1+p2)//2][-1]<=val:
            search(t,val,(p1+p2)//2, p2)
        else:
            search(t,val, p1, (p1+p2)//2)
    else:
        if t[0][-1]>val:
            t[0].append(val)
            return t
        else:
            t.append([val])
            return t

for i, val in enumerate(a[1:]):
    p1=0
    p2=len(towers)
    search(towers, val, p1, p2)
print(len(towers))
