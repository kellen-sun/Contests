a = int(input())
c = []
d = []
for x in range(a):
    b = input('')
    e = b.split(",")
    c.append(int(e[0]))
    d.append(int(e[1]))
f, g, h, i = max(c)+1, min(c)-1, max(d)+1, min(d)-1
print(str(g) + ',' + str(i))
print(str(f) + ',' + str(h))
