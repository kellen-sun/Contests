import sys
import heapq
input = sys.stdin.readline

n = int(input())
clubs = [int(input()) for i in range(int(input()))]
count = [-1 for i in range(n+1)]
for i in clubs: count[i]=1
for i in range(len(count)):
    if count[i]==-1:
        consider = []
        for j in clubs:
            if i-j>=0:
                if count[i-j]!=-1:
                    consider.append(count[i-j])
        if consider:
            count[i]=min(consider)+1
if count[n]==-1:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in", count[n], "strokes.")