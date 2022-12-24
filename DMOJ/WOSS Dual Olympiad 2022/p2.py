n = int(input())
print(*list(range(n, 0, -1)))
if n>1:
    l=list(range(1,n+1))
    l.pop(1)
    l.append(2)
    print(*l)
else:
    print(1)