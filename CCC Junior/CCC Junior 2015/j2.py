a = input('')
b = int(a.count(':-)'))
c = int(a.count(':-('))
if c==0 and b==0:
    print('none')
elif b>c:
    print('happy')
elif c>b:
    print('sad')
elif b == c:
    print('unsure')
