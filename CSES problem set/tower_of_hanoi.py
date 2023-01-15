n=int(input())
right = []
middle = []
left = [i for i in range(n,0,-1)]

all_moves=[]
def move(d,a,b):
    if d==1:
        b.append(a.pop(-1))
    else:
        a.append(b.pop(-1))
    
    return a,b,d

def possible_moves(a,b):
    if len(a)==0:
        return 2
    elif len(b)==0:
        return 1
    elif b[-1]>a[-1]:
        return 1 #a,b
    else:
        return 2 #b,a
print(2**n-1)

if n%2==0:
    for x in range(2**n-1):
        if x%3 == 0:
            left, middle,d=move(possible_moves(left, middle),left, middle)
            if d==1:
                all_moves.append('1 2')
            else:
                all_moves.append('2 1')
        elif x%3 == 1:
            left, right,d=move(possible_moves(left, right),left, right)
            if d==1:
                all_moves.append('1 3')
            else:
                all_moves.append('3 1')
        elif x%3 == 2:
            middle, right,d=move(possible_moves(middle, right),middle, right)
            if d==1:
                all_moves.append('2 3')
            else:
                all_moves.append('3 2')
else:
    for x in range(2**n-1):
        if x%3 == 0:
            left, right,d=move(possible_moves(left, right),left, right)
            if d==1:
                all_moves.append('1 3')
            else:
                all_moves.append('3 1')
        elif x%3 == 1:
            left, middle,d=move(possible_moves(left, middle),left, middle)
            if d==1:
                all_moves.append('1 2')
            else:
                all_moves.append('2 1')
        elif x%3 == 2:
            middle, right,d=move(possible_moves(middle, right),middle, right)
            if d==1:
                all_moves.append('2 3')
            else:
                all_moves.append('3 2')
for x in all_moves:
    print(x)    

