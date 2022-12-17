n=int(input())
array = [int(input()) for i in range(n)]
print(min(sum(array)-max(array), sum(array)//2))