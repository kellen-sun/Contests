

count=0
for i in range(1,2023):
    for j in range(1,2023):
        k = (i**2+j**2)**0.5
        if i+j+k<=2023 and i**2+j**2==k**2 and k == int(k) and i+j>k:
            count+=1
print(count/2)

count=0
array = list(map(int, input().split()))
for i in array:
    if i%9 != 0:
        count+=1
print(count)

def count(string):
    a,b,c = 0,0,0
    for jj in string:
        if jj=="A":
            a+=1
        elif jj=="B":
            b+=1
        elif jj=="C":
            c+=1
    return a,b,c
cc=0
array=[input() for i in range(100000)]

for i in array:
    a,b,c = count(i)
    if a>=2 or b>=2 or c>=2:
        cc+=1
print(len(array)-cc)