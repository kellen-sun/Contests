n = int(input())
factors, i = [], 2
while i*i<=n:
    if n%i==0:
        factors.append(i)
        if i*i!=n: factors.append(n//i)
    i+=1
coprime = []    
for i in range(1,n):
    f = True
    for j in factors:
        if i%j==0: f=False
    if f: coprime.append(i)
p=1
for i in coprime:
    p*=i
p=p%n
if p == 1:
    print(len(coprime))
    print(*coprime)
else:
    coprime.remove(p)
    print(len(coprime))
    print(*coprime)
