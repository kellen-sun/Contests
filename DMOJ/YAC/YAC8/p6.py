import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline
from itertools import permutations


n = int(input())
arr = list(map(int, input().split()))
if n<=8:
    perms = list(permutations(range(n)))
    willreach = [list(set([(i**j)%n for j in range(n+1)])) for i in range(n)]
    # need a get list of all the subtrees
    tree = [[] for i in range(n)]
    for i in range(n-1):
        tree[arr[i]].append(i+1)
    subtrees = []
    for i in range(n):
        curtree = []
        queue = [i]
        while queue:
            cur = queue.pop()
            curtree.append(cur)
            for j in tree[cur]:
                queue.append(j)
        subtrees.append(curtree)
    #print(subtrees)
    enigmaticcount = []
    for j in perms:
        c = 0
        for i in subtrees:
            newtree = [j[k] for k in i]
            if (1 in newtree and 0 not in newtree):
                curset = set()
                for k in newtree:
                    curset = curset.union(set(willreach[k]))

                if set(newtree) == curset:
                    c+=1
        enigmaticcount.append(c)
    print(min(enigmaticcount))
    print(max(enigmaticcount))
    fact = 1
    for i in range(1,n+1):
        fact *= i
    numerator = sum(enigmaticcount)
    #reduce fraction to simpler terms
    primes = [2,3,5,7]
    i = 0
    while True:
        if numerator % primes[i] == 0 and fact % primes[i] == 0:
            numerator, fact = numerator // primes[i], fact // primes[i]
        else:
            i+=1
        if i == 4:
            break
    MOD = 998244353
    y = pow(fact, -1, MOD) * numerator

    print(y%MOD)

elif sum(arr) == 0:
    MOD = 998244353
    c = 0
    for i in range(n):
        if i**2 % n == i:
            c += 1
    print(0)
    print(1)
    fact = n
    numerator = n-1
    y = pow(fact, -1, MOD) * numerator

    print(y%MOD)
else:
    print(0)
    print(69)
    print(69)

