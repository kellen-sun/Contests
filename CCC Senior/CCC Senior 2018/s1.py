n=int(input())
villages=[]

for x in range(n):
    villages.append(int(input()))
villages=sorted(villages)
neighborhood_size=[0]*len(villages)
for x in range(len(villages)-1):
    neighborhood_size[x]+=(villages[x+1]-villages[x])/2
    neighborhood_size[x+1]+=(villages[x+1]-villages[x])/2
print(min(neighborhood_size[1:-1]))
