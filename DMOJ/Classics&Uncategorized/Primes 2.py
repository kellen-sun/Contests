n, m = map(int, input().split())
#segmented sieve
from array import array
lim = int(m**0.5)
primes = array("L", [2])
primes2 = array("B")

for i in range(lim+1):
    primes2.append(0)

for i in range(2, lim+1):
    if not primes2[i]:
        primes.append(i)
        for j in range(i*i, lim+1, i):
            primes2[j]=1

sieve = array("B")
for i in range(n, m+1):
    sieve.append(1)

for i in primes:
    for j in range(max(i*i, (n+i-1)//i*i), m+1, i):
        sieve[j-n] = 0
if n==1:
    sieve[0]=0
for i in range(n, m+1):
    if sieve[i-n]:
        print(i)
