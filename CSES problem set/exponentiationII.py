for i in range(int(input())):
	first, second, third = [int(i) for i in input().split()]
	print(pow(first, pow(second, third, 1000000006), 1000000007))
