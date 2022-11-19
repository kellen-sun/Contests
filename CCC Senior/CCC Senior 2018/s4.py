n=int(input())
checked={'1':1,'2':1}
def check(n,checked):
    total=0
    if str(n) in checked.keys(): return checked[str(n)]
    for x in range(n,1,-1):
        total+=check(n//x,checked)
    checked[str(n)]=total
    return total
for x in range(n):
    print(check(x,checked))
