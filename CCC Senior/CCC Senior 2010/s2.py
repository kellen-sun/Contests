n = int(input())
code = {}
for i in range(n):
    a=input().split()
    code[a[1]]=a[0]
t = input()
c = ""
o = ""
for i in t:
    c=c+i
    if c in list(code.keys()):
        o=o+code[c]
        c=""
print(o)
