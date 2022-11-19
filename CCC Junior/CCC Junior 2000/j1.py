days=list(map(int, input().split()))
print("Sun Mon Tue Wed Thr Fri Sat")
weeks=[[]]
current_day = days[0]-1
for i in range(1,1+days[1]):
    if current_day == 7:
        weeks.append([i])
        current_day=1
    else:
        weeks[-1].append(i)
        current_day+=1
s=""
for i in weeks[0]:
    s=s+"   "+str(i)
if days[0]==1:
    print(s[1:])
else:
    print(((7-len(weeks[0]))*4-1)*" "+s)
for i in range(1, len(weeks)):
    s=""
    for j in weeks[i]:
        s=s+" "*(4-len(str(j)))+str(j)
    print(s[1:])
