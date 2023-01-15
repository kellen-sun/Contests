n=int(input())
s=n*(n+1)//2
x = list(range(1, n + 1))
if s % 2 == 0:
    print("YES")
    half = s // 2
    a = set()
    b = set()
    for i in range(n, 0, -1):
        if i <= half:
            half -= i
            a.add(i)
        else:
            b.add(i)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
else:
    print('NO')
