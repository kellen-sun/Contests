left = 0
right = 0
n,m = map(int, input().split())
array = list(map(int, input().split()))

s = array[0]
minimum = 100000000000
while True:
    if s>=m:
        if right-left+1<minimum:
            minimum = right-left+1
        s-=array[left]
        left+=1
    if right == n-1 and s<m:
        break
    if s<m:
        right+=1
        s+=array[right]

if minimum==100000000000:
    print(-1)
else:
    print(minimum)