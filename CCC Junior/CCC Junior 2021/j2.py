n=int(input())
m=0
winner=""
for i in range(n):
    name = input()
    bid = int(input())
    if bid>m:
        m=bid
        winner = name
print(winner)