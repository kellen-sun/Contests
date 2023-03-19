n=int(input())
a=list(map(int, input().split()))
if sorted(a)==list(range(1,n+1)):
    print(1)
else:
    print(-1)
#it's possible if the given array is a permutation of the array 1,2,3,4...n
