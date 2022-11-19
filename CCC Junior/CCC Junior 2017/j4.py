def mtot(m):
    if (m//60)-((m//60)//12)*12==0:
        return int('12'+str(m-(m//60)*60))
    else:
        return int(str((m//60)-((m//60)//12)*12)+ str(m-(m//60)*60))
times=[111, 123, 135, 147, 159, 210, 222, 234, 246, 258, 321, 333, 345, 357, 420,432,444,456,
531, 543,555,630,642,654,741,753,840,852, 951,1111, 1234
]
a=int(input())
counter=0
if mtot(a-(a//720)*720)>1200:
    if mtot(a-(a//720)*720)>=1234:
        counter+=1
else:
    for x in times:
        if mtot(a-(a//720)*720)>=x:
            counter+=1
print(counter+(a//720)*len(times))
