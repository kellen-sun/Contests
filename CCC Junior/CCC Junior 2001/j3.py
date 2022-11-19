cards=input('Enter cards: ')
card_list=[]
for x in range(len(cards)):
    card_list.append(cards[x])
print('Cards dealt          Points')
clubs=[]
diamonds=[]
hearts=[]
spades=[]
for x in range(len(card_list)):
    if card_list[x]=='D':
        clubs=card_list[:x]
        c=x
        break
for x in range(len(card_list)):
    if card_list[x]=='H':
        diamonds=card_list[c:x]
        c=x
        break
for x in range(len(card_list)):
    if card_list[x]=='S':
        hearts=card_list[c:x]
        break
for x in range(len(card_list)):
    if card_list[x]=='S':
        spades=card_list[x:]
        break

c_points=0
d_points=0
h_points=0
s_points=0

if len(clubs)==1:
    c_points+=3
elif len(clubs)==2:
    c_points+=2
elif len(clubs)==3:
    c_points+=1
    
if len(diamonds)==1:
    d_points+=3
elif len(diamonds)==2:
    d_points+=2
elif len(diamonds)==3:
    d_points+=1

if len(hearts)==1:
    h_points+=3
elif len(hearts)==2:
    h_points+=2
elif len(hearts)==3:
    h_points+=1
    
if len(spades)==1:
    s_points+=3
elif len(spades)==2:
    s_points+=2
elif len(spades)==3:
    s_points+=1

def add_points(clubs, c_points):
    for x in range(len(clubs)):
        if clubs[x]=='A':
            c_points+=4
        elif clubs[x]=='K':
            c_points+=3
        elif clubs[x]=='Q':
            c_points+=2
        elif clubs[x]=='J':
            c_points+=1
    return c_points

print(add_points(clubs, c_points))
print(add_points(diamonds, d_points))
print(add_points(hearts, h_points))
print(add_points(spades, s_points))
    
print('Total: '+str(add_points(spades, s_points)+add_points(hearts, h_points)+add_points(diamonds, d_points)+add_points(clubs, c_points)))
