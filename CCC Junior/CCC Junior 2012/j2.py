b=[]
for x in range(4):
    a = int(input())
    b.append(a)
c=b[:]
if b[0]==b[1] and b[1]==b[2] and b[2]==b[3]:
    print('Fish At Constant Depth')
elif b[0]<b[1] and b[1]<b[2] and b[2]<b[3]:
    print('Fish Rising')
elif b[0]>b[1] and b[1]>b[2] and b[2]>b[3]:
    print('Fish Diving')
else:
    print('No Fish')
