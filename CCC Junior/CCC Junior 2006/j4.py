from itertools import permutations
requirements = [[1,7], [1,4], [2,1], [3,4], [3,5]]
while True:
    c=int(input())
    d=int(input())
    a = [c,d]
    if a == [0,0]:
        break
    else:
        requirements.append(a)

pos = list(range(1,8))
def check(i):
    global requirements
    success = True
    for j in requirements:
        if not (i[j[0]-1] < i[j[1]-1]):
            success = False
    return success
fail = True
#print(requirements)
possible_out = []
for i in permutations(pos):
    if check(i):
        #print(*i)
        out = [0 for i in range(7)]
        for k in range(7):
            out[i[k]-1]=k+1
        possible_out.append(out)
        fail = False
if fail: print("Cannot complete these tasks. Going to bed.")
else: print(*sorted(possible_out)[0])
