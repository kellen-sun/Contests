x= input().split()
y= input().split()
a, b, c, d = int(x[0]), int(x[1]), int(y[0]), int(y[1])
t=int(input())
if (t-abs(a-b)+abs(c-d))%2 == 0 and t-abs(a-c)-abs(b-d)>=0:
    print('Y')
else:
    print('N')
