def phi(M):
    #find phi in root N time
    prime_factors = set()
    checker = 2
    prod = M
    while True:
        if M==1:
            break
        if checker**2>M:
            prime_factors.add(M)
            break
        if M%checker==0:
            M=M//checker
            prime_factors.add(checker)
        else:
            checker+=1
    for p in prime_factors:
        prod*=(1-1/p)
    return int(prod)

def checkgreater(a, b, mod):
    c = a
    counter = 1
    if a==1:
        return True
    while True:
        #should only loop like 30 times at most if base is 2
        if c>=mod:
            return False
        if counter>=b:
            return True
        c*=a
        counter+=1


N,M = map(int, input().split())
array = list(map(int, input().split()))

totients = [M]
while True:
    totients.append(phi(totients[-1]))
    if totients[-1]==1 or len(totients)==N+2:
        break

if N==1:
    print(array[0]%M)
else:
    if N<len(totients):
        if array[-1]>=totients[N-1]:
            array[-1]=array[-1]%totients[N-1]+totients[N-1]
    else:
        array[-1]=1
    while len(array)>2:
        if len(array)<len(totients):
            totient = totients[len(array)-2]
            last = array.pop()
            slast = array.pop()
            temp = pow(slast, last, totient)
            if checkgreater(slast, last, totient):
                array.append(temp)
            else:
                array.append(temp+totient)
        else:
            array.pop()
            array.pop()
            array.append(1)
        #print(array)
    print(pow(array[0], array[1], M))


