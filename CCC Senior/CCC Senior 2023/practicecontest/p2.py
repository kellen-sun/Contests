n = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))
pre1 = [0]
pre2 = [0]
s1 = 0
s2 = 0
for i in range(n):
    s1+=team1[i]
    s2+=team2[i]
    pre1.append(s1)
    pre2.append(s2)
for i in range(n, -1, -1):
    if pre1[i]==pre2[i]:
        print(i)
        break