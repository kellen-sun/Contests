n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    c = 0
    current = i+1
    visited = []
    while current not in visited:
        visited.append(current)
        c+=1
        current = a[current-1]
    print(c, end=" ")
