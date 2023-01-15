a=int(input())
if a==1:
    print('1')
elif a==4:
    print('2 4 1 3')
elif a<5:
    print('NO SOLUTION')
else:
    b=[]
    if a%2==0:
        for x in range(1,a+1,2):
            b.append(x)
        b.append(a-4)
        b.append(a-2)
        b.append(a)
        for x in range(a-6,1,-2):
            b.append(x)
    else:
        for x in range(1,a+1,2):
            b.append(x)
        b.append(a-3)
        b.append(a-1)
        for x in range(a-5,0,-2):
            b.append(x)
    print(*b)
