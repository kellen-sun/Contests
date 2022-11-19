n=int(input())
computers = [list(input().split()) for i in range(n)]
c={}
for i in computers:
    c[int(i[1])*2+int(i[2])*3+int(i[3])]=i[0]

first=0
f_n = ""
second=0
s_n = ""
for i in list(c.keys()):
    if i>first:
        second = first
        s_n = f_n
        f_n = c[i]
        first = i
    elif i>second:
        second = i
        s_n=c[i]
    elif i==first and i==second:
        if c[i]<f_n:
            if f_n<s_n:
                s_n=f_n
            f_n=c[i]
        elif c[i]<s_n:
            s_n=c[n]
    elif i==second:
        if c[i]<s_n:
            s_n=c[i]
    
if s_n!="":
    print(f_n)
    print(s_n)
else: print(f_n)
