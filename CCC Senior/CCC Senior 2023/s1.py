n = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

c = 0
for i in row1:
    if i==1:
        c+=3

for i in row2:
    if i==1:
        c+=3

for i in range(n):
    if row1[i]==row2[i] and row1[i]==1 and i%2==0:
        c-=2
for i in range(n-1):
    if row1[i]==row1[i+1] and row1[i]==1:
        c-=2
for i in range(n-1):
    if row2[i]==row2[i+1] and row2[i]==1:
        c-=2

print(c)