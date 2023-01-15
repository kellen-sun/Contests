q=list(map(int, input().split()))[1]
array=list(map(int, input().split()))
queries=[]
for x in range(q):
    queries.append(list(map(int, input().split())))
summed=0
sums=[]
for x in array:
    summed+=x
    sums.append(summed)
sums.append(0)
for query in queries:
    
    print(sums[query[1]-1]-sums[query[0]-2])
