k = int(input())
def largest_component(n):
    return int((1+(1+8*n)**0.5)//2)
component_size = []

while k>0:
    m = largest_component(k)
    component_size.append(m)
    k=k-m*(m-1)//2

#print(component_size)
print(sum(component_size), sum(component_size)+len(component_size)-1)
edges = []
comp_start = 1
for i in range(len(component_size)):
    comp_current = comp_start
    for j in range(component_size[i]):
        edges.append((j+comp_current, comp_current+(j+1)%component_size[i]))
    comp_start+=j+1
    edges.append((comp_start,comp_current))
for i in edges[:-1]: print(*i)