var = {"A":0, "B":0}
out = []

while True:
    c=input()
    if c=="7":
        break
    if c[0]=="1":
        var[c[2]]=int(c[4:])
    if c[0]=="2":
        out.append(var[c[2]])
    if c[0]=="3":
        var[c[2]]=var[c[2]]+var[c[4]]
    if c[0]=="4":
        var[c[2]]=var[c[2]]*var[c[4]]
    if c[0]=="5":
        var[c[2]]=var[c[2]]-var[c[4]]
    if c[0]=="6":
        var[c[2]]=var[c[2]]//var[c[4]]

for i in out:
    print(i)