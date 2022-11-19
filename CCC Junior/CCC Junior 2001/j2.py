x=int(input('Enter x: '))
m=int(input('Enter m: '))
j=False
for n in range(m):
    if x*n%m==1:
        print(n)
        j=True
    
if not j:
    print('No such integer exists.')
