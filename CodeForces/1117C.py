start = list(map(int, input().split()))
end = list(map(int, input().split()))
n = input()
wind = input()
low = 0
high = 2 * 10**14
v=-1

def f(start, end, wind, time):
    start = start.copy()
    x = wind.count("R")-wind.count("L")
    y = wind.count("U")-wind.count("D")
    c = time//len(wind)
    x *= c
    y *= c
    r = time%len(wind)
    wind = wind[:r]
    x += wind.count("R")-wind.count("L")
    y += wind.count("U")-wind.count("D")
    start[0]+=x
    start[1]+=y
    return abs(start[0]-end[0])+abs(start[1]-end[1])<=time

while low<=high:
    mid = (low+high)//2
    if f(start, end, wind, mid):
        v = mid
        high = mid-1
    else:
        low = mid+1
print(v)
