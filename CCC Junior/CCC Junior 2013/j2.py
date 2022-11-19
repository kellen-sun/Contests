allowed=['I', 'O', 'S', 'H', 'Z', 'X', 'N']
a,b=True,input()
for x in b:
    if x not in allowed:
        a=False
        print('NO')
        break
if a:
    print('YES')
