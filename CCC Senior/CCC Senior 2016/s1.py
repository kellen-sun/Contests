from collections import Counter
a=Counter(input())
b=Counter(input())
out="A"
for i in b.keys():
    if i!="*" and b[i]>a[i]: out="N"
print(out)
