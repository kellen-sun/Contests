b=[]
for x in range(4):
    a = int(input())
    b.append(a)
c=b[:]
if b[0]==b[1] and b[1]==b[2] and b[2]==b[3]:
    print('constant')
elif b == sorted(b):
    print('rise')
elif b == sorted(b, reverse=True):
    print('descending')
else:
    print('no fish')
