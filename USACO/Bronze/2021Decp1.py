n = int(input())
cows = list(input())
h,g,ans,p1,p2 = 0,0,0,0,0
psumh=[0]
c=0
for i in cows:
    if i=="H":
        c+=1
    psumh.append(c)
psumg=[0]
c=0
for i in cows:
    if i=="G":
        c+=1
    psumg.append(c)
for i in range(n):
    for j in range(i+1,n+1):
        if (psumh[j]-psumh[i]==1 or psumg[j]-psumg[i]==1) and len(cows[i:j])>2:
            #print(cows[i:j])
            ans+=1

'''        
psumh=[0]
c=0
for i in cows:
    if i=="H":
        c+=1
    psumh.append(c)
#print(psumh)
for i in range(n+1):
    if psumh[i]-psumh[p1]==1:
        while psumh[i]-psumh[p1]==1:
            #print(p1,i)
            if i-p1>2:
                ans+=1
                p1+=1
            else:
                break
    elif psumh[i]-psumh[p1]>1:
        while psumh[i]-psumh[p1]>1:
            p1+=1
#print(ans)
psumh=[0]
c=0
p1=0
for i in cows:
    if i=="G":
        c+=1
    psumh.append(c)
#print(psumh)
for i in range(n+1):
    if psumh[i]-psumh[p1]==1:
        while psumh[i]-psumh[p1]==1:
            
            if i-p1>2:
                #print(p1,i)
                ans+=1
                p1+=1
            else:
                break
    elif psumh[i]-psumh[p1]>1:
        while psumh[i]-psumh[p1]>1:
            p1+=1 
'''            
print(ans)
