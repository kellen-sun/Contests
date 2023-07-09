n = int(input())
m = int(input())-1
#segmented sieve

#from array import array

lim = int(m**0.5)
primes = [2]

primes2 = bytearray(lim//8+1)

for i in range(2, lim+1):
    if primes2[i//8] & 2**(7-(i%8))==0:
        primes.append(i)
        for j in range(i*i, lim+1, i):
            if primes2[j//8] & 2**(7-(j%8))==0:
                primes2[j//8]+=2**(7-(j%8))

sieve = bytearray((m-n)//8+1)

for i in primes:
    for j in range(max(i*i, (n+i-1)//i*i), m+1, i):
        if sieve[(j-n)//8] & 2**(7-((j-n)%8)) == 0:
            sieve[(j-n)//8] = sieve[(j-n)//8] + 2**(7-((j-n)%8))

if n==1:
    sieve[0]+=2**7
count = 0

for i in sieve:
    count+=bin(i).count('1')
print(m+1-n-count)