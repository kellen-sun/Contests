a=int(input())
b=int(input())
c=int(input())
d=int(input())
s=int(input())

nikky = [1 for i in range(a)]+[-1 for j in range(b)]
byron = [1 for i in range(c)]+[-1 for j in range(d)]
pos_n=0
pos_b=0

for i in range(s):
    pos_n+=nikky[i%(a+b)]
    pos_b+=byron[i%(c+d)]

if pos_b>pos_n:
    print("Byron")
elif pos_n>pos_b:
    print("Nikky")
else:
    print("Tied")