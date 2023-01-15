n = int(input())
a = [float('inf')]*(n+2)
for i in range(len(a)):
    if i<10:
        a[i]=1
    else:
        a[i]=min(list(a[i-int(j)] for j in str(i)))+1
print(a[n])
