n = int(input())
out = []
for i in range(n):
    k = input().split()
    for i in k:
        if len(i)==7:
            if i[2]=="/" and i[5]=="/":
                dd = i[:2]
                mm = i[3:5]
                yy = i[6:8]
            if i[2]=="." and i[5]==".":
                yy = i[:2]
                mm = i[3:5]
                dd = i[6:8]
                if yy.isdigit() and mm.isdigit() and yy.isdigit():
                    d,m,y = int(dd), int(mm), int(yy)
