x=int(input())
same=[tuple(input().split()) for i in range(x)]
y=int(input())
different=[tuple(input().split()) for i in range(y)]
g=int(input())
groups={}
for i in range(g):
    a,b,c = tuple(input().split())
    groups[a]=i
    groups[b]=i
    groups[c]=i

c=0
for constraint in same:
    s1,s2=constraint
    if groups[s1]!=groups[s2]: c+=1
for constraint in different:
    s1,s2=constraint
    if groups[s1] == groups[s2]: c+=1
print(c)
