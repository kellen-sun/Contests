import sys
#import heapq
from collections import deque, Counter
input = sys.stdin.readline

n, q = map(int, input().split())
#array = [0 for i in range(n)]
queries = []
for iii in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1 or query[0] == 2:
        queries.append(query)
    if query[0] == 3:
        c = 0
        interest = query[1]
        for i in queries:
            if i[1]<=interest and interest<=i[2]:
                if (interest-i[1])%i[3]==0:
                    if i[0]==1:
                        c+=i[4]
                    if i[0]==2:
                        c=i[4]
        #print(queries)
        print(c)