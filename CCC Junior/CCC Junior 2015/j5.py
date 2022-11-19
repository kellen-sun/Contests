n=int(input())
k=int(input())
lookup={}
def pie_counter(n,k,j):
    global lookup
    if k==n or k==1:
        return 1
    elif k==0:
        return 0
    else:
        s=0
        for i in range(j, n//k+1):
            if (n-i, k-1, i) in lookup.keys():
                s+=lookup[(n-i, k-1, i)]
            else:
                cur = pie_counter(n-i, k-1, i)
                lookup[(n-i,k-1, i)]=cur
                s+=cur
        return s
print(pie_counter(n,k,1))