#nrootn too slow
#segmented sieve Memory error, because root(10^18) ~ 10^9 ~ 1GB of memory
#millers random prime test

n = int(input())
import random
def check_prime(k):
    if k==1:
        return False
    if k==2:
        return True
    if k==3:
        return True
    if k%2==0:
        return False
    #consider all n>2 (odd)
    s=0
    d=k-1
    while True:
        if d%2==0:
            s+=1
            d//=2
        else: break
    testcount = 35
    for i in range(testcount):
        a = random.randint(2, k-2)
        x= pow(a, d, k)
        for j in range(s):
            y = pow(x, 2, k)
            if y==1 and x!=1 and x!=(k-1):
                return False
            x=y
        if y!=1:
            return False
        return True
i=n
while True:
    if check_prime(i):
        print(i)
        break
    i+=1
