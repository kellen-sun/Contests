a = int(input())
b = input()
B=0
for x in range(0, a):
    if b[x]=='B':
        B+=1
if B>a//2:
    print('B')
elif B==a//2 and a%2==0:
    print('Tie')
else:
    print('A')
