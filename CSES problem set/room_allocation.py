from queue import PriorityQueue


n = int(input())
a = sorted([tuple(map(int, input().split()))[::-1] for i in range(n)], key = lambda x:x[1])
#print(a)
q = PriorityQueue()
m = 1
q.put(a[0])
ans = [1]
for i in range(1,len(a)):
    t=q.get()
    if a[i][1]>t[0]:
        q.put(a[i])
        ans.append(1)
    else:
        q.put(t)
        q.put(a[i])
        ans.append(q.qsize())
    if q.qsize()>m:
        m=q.qsize()
print(m)
print(*ans)
