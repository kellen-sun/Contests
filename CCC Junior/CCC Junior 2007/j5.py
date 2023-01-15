a=int(input())
b=int(input())
n=int(input())
motels=[0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
new_motels=[]
for x in range(n):
	new_motels.append(int(input()))
motels = motels + new_motels
motels.sort()
values={}

def dp(motels, place, a, b):
	if place==motels[-1]:
		return 1
	elif place in values.keys():
		return values[place]
	else:
		current=0
		for x in motels:
			if x>=place+a and x<=place+b:
				current+=dp(motels,x,a,b)
		values[place]=current
		return current		
print(dp(motels, 0, a, b))
