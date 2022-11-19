from itertools import compress, product

def combinations(items):
    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )
people={}
a=int(input(''))
for b in range(1, a):
    c=int(input(''))
    if c in people.keys():
        people[c].append(b)
    else:
        people[c]=[b]
remove_sets=[]
def remove(people, person, removed):

    d=people.pop(person, [])
    removed.append(person)
    for i in range(len(d)):
        if d[i] not in removed:
            removed.append(d[i])
        removed=remove(people, d[i], removed)

    return removed
    
z=list(combinations(range(1, a)))

for x in range(len(z)):
    v=[]
    for l in range(len(z[x])):
        removed=[]
        f=dict(people)
        v=list(set(remove(f, list(z[x])[l], removed)).union(set(v)))
    if v not in remove_sets:
        remove_sets.append(v)
print(len(remove_sets))
