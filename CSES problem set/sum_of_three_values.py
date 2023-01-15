import sys
 
n,x = map(int,input().split())
a = [int(x) for x in input().split()]
 
val_to_ind = {}
for i,val in enumerate(a):
	val_to_ind[val] = i+1
for ind1,i in enumerate(a):
    for ind2,j in enumerate(a):
        if x-i-j in val_to_ind:
            if ind1+1!=ind2+1 and ind1+1!=val_to_ind[x-i-j] and ind2+1!=val_to_ind[x-i-j]:
                print(ind1+1, ind2+1, val_to_ind[x-i-j])
                sys.exit(0)
print("IMPOSSIBLE")
