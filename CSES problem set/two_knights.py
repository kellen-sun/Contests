n=int(input())
all_n=[0,6,28,96]
for x in range(5,n+1):
	b=all_n[-1]
	all_n.append(int(b+(x-1)**2*(2*x-1)+(2*x-1)*(2*x-2)/2-(20+(x-4)*4+(x-5)*4)))
print(*all_n[:n], sep='\n')
