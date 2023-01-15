input()
a = list(map(int, input().split()))
divisors = [0]*(int(1e6)+1)
for i in a:
    for j in range(1, int(i**0.5)+1):
        if i%j==0:
            divisors[j]+=1
            if not j**2 == i:
                divisors[i//j]+=1
#print(divisors)
for i in range(len(divisors)-1,0,-1):
    if divisors[i] > 1:
        print(i)
        break
