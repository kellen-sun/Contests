a=[int(input()) for i in range(int(input()))]
if sum(a)%2==0 and max(a)<=sum(a)/2: print("YES")
else: print("NO")