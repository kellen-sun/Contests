a = input()
b = input()
c = False
for x in range(len(b)):
    if a.find(b) != -1:
        c = True
    b = b[1:-1] + b[-1] + b[0]
if c == True:
    print('yes')
else:
    print('no')
