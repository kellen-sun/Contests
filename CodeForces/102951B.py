n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
t=0
c=0
#use while loop
while t<x:
    t+=a[c]
    c+=1
print(c-1)
