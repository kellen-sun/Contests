import sys
a=[]
b=[]
n = int(input())
for i in range(1,n):
    print(i,i)
    sys.stdout.flush()
    x = input()
    if x=="-1":
        sys.exit()
    temp = list(map(int, x.split()))
    a.append(temp[0])
    b.append(temp[1])
    if temp[0]==temp[1]:
        sys.exit()
b.append(n*(n+1)//2-sum(b))
for j in range(len(b)):
    if a[0]==b[j]:
        print(1,j+1)
        sys.stdout.flush()
        break