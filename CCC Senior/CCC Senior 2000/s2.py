n = int(input())
flow = [float(input()) for i in range(n)]
while True:
    k = int(input())
    if k==77:
        break
    if k==99:
        i = int(input())
        percent = int(input())
        ff = flow[i-1]
        flow[i-1]=ff*percent/100
        flow.insert(i, ff-ff*percent/100)
    if k==88:
        i = int(input())
        flow[i-1]=flow[i-1]+flow.pop(i)
print(*map(int, flow))