n=int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))
tot = 0
for i in range(len(widths)):
    tot+=widths[i]*(heights[i]+heights[i+1])
print(tot/2)