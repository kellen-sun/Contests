a=input()
current=''
number=0
record=0
for x in a:
	if x==current:
		number+=1
		if number>record:
			record=number
	else:
		current=x
		number=0
print(record+1)
