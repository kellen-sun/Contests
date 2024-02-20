import sys
import itertools
#import heapq
from collections import deque, Counter
input = sys.stdin.readline
import math

MOD = 10**9 + 7
n, d = map(int, input().split())

factn = [1]
for i in range(1, n+1):
    factn.append(factn[-1] * i % MOD)
def fact(n):
    return factn[n]
#print("done fac")
#def choose(n,k):
    #return math.comb(n, k) % MOD


m = n-d
permm = [1]
for i in range(1, n//2+1):
    permm.append(permm[-1]*(m+1 - i) % MOD)
def perm(k):
    return permm[k]
#print("Done perm")
pow2 = [1]
for i in range(n+1):
    pow2.append(pow2[-1]*2%MOD)
#print("done pow")
choosen = [1]
# choosen[x] should give (n-x choose x)
for i in range(1, n//2+1):
    var1 = pow(i,-1, MOD)
    var2 = var1*pow(n-i+1,-1, MOD)%MOD
    choosen.append(choosen[-1]*var2*(n-2*i+1)*(n-2*i+2)%MOD)
#print("done choose")
def helper(n, d, x):
    # at least x jumps of size (exactly) d
    # n-d options of jumps
    # 2**x (n-d choose x) * x!
    # n-2x remaining numbers to randomly organize after
    # (n-2x)!
    # choose placements of jumps:
    # (n-x choose x)
    # compute all MOD
    #print(pow(2, x, MOD), perm(x), fact(n-2*x), choose(n-x, x))
    return pow2[x] * perm(x) * fact(n-2*x) * choosen[x] % MOD

s = 0
sign = 1
for i in range(1, n//2+1):
    s = (s+ sign*helper(n, d, i))%MOD
    sign = -sign

print(s)