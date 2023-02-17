n = int(input())
'''
array = [True for i in range(n+1)]

for i in range(n+1):
    for j in range(1, 19):
        if i%3**(j+1)<2*3**j and i%3**(j+1)>3**j:
            array[i]=False
            break

for i in range(n+1):
    if array[i]: print(i)
'''
array2 = []
def rec(a,b):
    if b-a == 3:
        array2.append(a)
        array2.append(a+1)
        array2.append(a+2)
        array2.append(b)
        return
    rec(a, (b-a)//3+a)
    rec(a+2*(b-a)//3, b)
rec(0,n)
for i in array2:
    print(i)