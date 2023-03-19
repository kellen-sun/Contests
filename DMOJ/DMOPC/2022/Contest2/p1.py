n=int(input())
if n<=6:
    if n%3==0:
        print(n//3)
        print((n//3)*"M__")
    else: 
        print((n+2)//3)
        print(2*"M"+(n-2)*"_")
else:
    if n%4==3:
        print((n//4)*2+1)

    else:
        print(2*(n//2))
        print((n//2+1)*"M__M"[:n])