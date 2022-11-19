a = int(input(''))
v = []
var = ''
for x in range(a):
    b = input('')
    l = b.split()
    for y in range(int(l[0])):
        var = var + l[1]
    v.append(var)
    var = ''
for z in range(a):
    print(v[z])
