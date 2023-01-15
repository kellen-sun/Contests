
a=int(input())
p=[]
for x in range(a):
	u=input().split()
	v=[int(u[0]), int(u[1])]
	y,x=v[0],v[1]
	m=max(v)
	if x>=y:
		if x%2==1:
			b=x**2+1-y
		else:
			b=(x-1)**2+y
	else:
		if y%2==1:
			b=(y-1)**2+x
		else:
			b=y**2+1-x
	p.append(b)
for x in p:
	print(x)
