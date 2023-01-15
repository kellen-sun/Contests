n=int(input())
a=sorted(list(map(int, input().split())))
x=a[n//2]
c=0
for i in a:
    c+=abs(x-i)
print(c)
