a=int(input())
b=[a]
while a!=1:
    if a%2==1: a=a*3+1
    else: a=int(a/2)
    b.append(a)
print(*b)
