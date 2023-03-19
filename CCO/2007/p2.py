import sys
input = sys.stdin.readline
n = int(input())
snowflakes = [[] for i in range(100000)]
for i in range(n):
    c=list(map(int, input().split()))
    snowflakes[sum(c)%100000].append(c)

def compare(a,b):
    for i in range(6):
        same = True
        for j in range(6):
            if a[j]!=b[(j+i)%6]:
                same = False
                break
        if same:
            return same
    for i in range(6):
        same = True
        for j in range(6):
            if a[j]!=b[(i-j)%6]:
                same = False
                break
        if same:
            return same
    return False

for grouping in snowflakes:
    for i in range(len(grouping)):
        for j in range(i):
            if compare(grouping[i], grouping[j]):
                print("Twin snowflakes found.")
                sys.exit()
print("No two snowflakes are alike.")