max_weight=int(input().split()[1])
people= list(map(int, input().split()))
seats=0

'''def min_max(people):
    
    for x in range(people):

while people:
    a=people.pop(people.index(max(people)))
    seats+=1
    for x in people:
        if x<=max_weight-a:
            people.remove(x)
            break'''
people=sorted(people)
top,bottom=0,-1
while -bottom+top<=len(people):
    #print(people)
    if people[bottom]+people[top]<=max_weight and len(people)>1:
        #people.pop(top)
        #people.pop(bottom)
        bottom-=1
        top+=1
    else:
        #people.pop(bottom)
        bottom-=1
    seats+=1

print(seats)
