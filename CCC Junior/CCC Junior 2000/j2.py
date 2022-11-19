m=int(input())
n=int(input())
c=0
for i in range(m, n+1):
    if "2" in str(i) or "3" in str(i) or "4" in str(i) or "5" in str(i) or "7" in str(i):
        pass
    else:
        ll=""
        for j in range(len(str(i))-1,-1,-1):
            if str(i)[j]=="6":
                ll=ll+"9"
            elif str(i)[j]=="9":
                ll=ll+"6"
            else:
                ll=ll+str(i)[j]
        if ll==str(i):
            c+=1
print(c)