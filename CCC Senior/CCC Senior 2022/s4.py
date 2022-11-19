n,c=map(int, input().split())
points=list(map(int, input().split()))
sol=0

def works(triangle, c):
    triangle=sorted(triangle)
    if (triangle[1]-triangle[0])%c<c/2 and (triangle[2]-triangle[1])%c<c/2 and (triangle[0]-triangle[2])%c<c/2 and triangle[0]!=triangle[1] and triangle[2]!=triangle[1] and triangle[0]!=triangle[2]:
        return True

working=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            triangle=(points[i], points[j],points[k])
            
            if works(triangle, c):
                working.append(str(sorted([i+1,j+1,k+1])))
                sol+=1
print(sol//6)
#print(list(set(working)))
