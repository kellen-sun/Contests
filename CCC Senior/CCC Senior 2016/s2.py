question=input()
n=int(input())

a=list(map(int, input().split()))
b=list(map(int, input().split()))
if question=="2": print(sum(sorted(a+b)[n:]))
else:
    a=sorted(a)
    b=sorted(b)
    s=0
    for i in range(n):
        s+=max(a[i],b[i])
    print(s)
