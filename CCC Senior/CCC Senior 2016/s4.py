def possiblemoves(array):
    moves=[]
    for i in range(len(array)-1):
        if array[i]==array[i+1]:
            a=array.copy()
            a[i]=2*array[i]
            a.remove(a[i+1])
            moves.append(a)
    for i in range(len(array)-2):
        if array[i]==array[i+2]:
            a=array.copy()
            a[i]=2*array[i]+array[i+1]
            a.remove(a[i+1])
            a.remove(a[i+1])
            moves.append(a)
    return moves

n=int(input())
arr=list(map(int, input().split()))
moves=[arr]
last=[]
while moves:
    current=moves.pop()
    p=possiblemoves(current)
    if p:
        for i in p:
            moves.append(i)
    else:
        last.extend(current)
print(max(last))
    
