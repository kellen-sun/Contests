shape=[
'*', 'x', '*',
' ', 'x', 'x',
'*', ' ', '*'
]
shape_2=[]
k =int(input())
for x in range(3):
    a=shape.pop(0)
    b=shape.pop(0)
    c=shape.pop(0)
    for h in range(k):
        shape_2.append([])
        s=x*k+h
        for y in range(k):
            shape_2[s].append(a)
        for y in range(k):
            shape_2[s].append(b)
        for y in range(k):
            shape_2[s].append(c)


for x in range(len(shape_2)):
    
    print(shape_2[x])
