n = int(input())
observations={}
for x in range(n):
    inp=tuple(map(int, input().split()))
    observations[inp[0]]=inp[1]
max_obs=0
sorted_keys=sorted(observations.keys())
for x in range(1,len(sorted_keys)):
    a=abs((observations[sorted_keys[x]]-observations[sorted_keys[x-1]])/(sorted_keys[x]-sorted_keys[x-1]))
    if a>max_obs:
        max_obs=a
    
    
print(max_obs)
