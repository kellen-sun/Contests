n,m,k=map(int, input().split())
if m==2:
    if (k>(2*n-1)) or (k<n):
        print(-1)
    else:
        if k==2*n-1:
            arr=[1,2]*n
            print(*arr[:n])
        else:
            if k%2==1:
                if n%2==1:
                    temp=(k-n)//2
                    arr=[1,2]*temp
                    ex=[1]*(2*n-k)
                    arr.extend(ex)
                    print(*arr)
                else:
                    temp=(k-n)//2
                    arr=[1,2]*temp
                    ex=[1]*(2*n-k)
                    arr.extend(ex)
                    arr.append(2)
                    print(*arr)
            else:
                if n%2==1:
                    temp=(k-n)//2
                    arr=[1,2]*temp
                    ex=[1]*(2*n-k)
                    arr.extend(ex)
                    arr.append(2)
                    print(*arr)
                else:
                    temp=(k-n)//2
                    arr=[1,2]*temp
                    ex=[1]*(2*n-k)
                    arr.extend(ex)
                    print(*arr)
                

else:
    goal = k-n
    out=[1]
    for i in range(1,n):
        if i-1>goal:
            
