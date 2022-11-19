array = [[1, 2], 
            [3,4]]

def V(array):
    a = array[0][0]
    c = array[0][1]
    b = array[1][0]
    d = array[1][1]
    array[0].clear()
    array[1].clear()
    array[0].append(c)
    array[0].append(a)
    array[1].append(d)
    array[1].append(b)
    return array
def H(array):
    a = array[0][0]
    c = array[0][1]
    b = array[1][0]
    d = array[1][1]
    array[0].clear()
    array[1].clear()
    array[0].append(b)
    array[0].append(d)
    array[1].append(a)
    array[1].append(c)
    return array
q = input('')
for d in range(len(q)):
    if q[d-1] == 'H':
        array = H(array)
    else: 
        array = V(array)
        
print(str(array[0][0]) + ' ' + str(array[0][1]))
print(str(array[1][0]) + ' ' + str(array[1][1]))
