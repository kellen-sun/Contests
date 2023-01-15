n = int(input())
positions = list(map(int, input().split()))
speed = list(map(int, input().split()))

def time(pos):
    global positions
    global speed
    global n
    m=0.0
    
    for i in range(n):
        if m<abs(positions[i]-pos)/speed[i]: 
            m=abs(positions[i]-pos)/speed[i]
            
    #print(m)
    return m

start = 0.0
end = float(1e10)
while start<=end:
    mid = (start+end)/2
    a = time(mid)
    b = time(mid+0.000001)
    c = time(mid-0.000001)
    print(c,a,b)
    print(mid)
    if c<=a and a<=b:
        end = mid-0.000001
    elif a>=c and b>=a: 
        start = mid+0.000001
    else:
        break
print(time(mid))
