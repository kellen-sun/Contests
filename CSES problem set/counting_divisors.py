MAX_N = 10 ** 6

max_div = [0 for _ in range(MAX_N + 1)]
for i in range(2, MAX_N + 1):
	if max_div[i] == 0:
		for j in range(i, MAX_N + 1, i):
			max_div[j] = i

ans = []
for _ in range(int(input())):
	n = int(input())
	div_num = 1
	while n != 1:
		largest = max_div[n]
		count = 0
		while n % largest == 0:
			count += 1
			n //= largest
		div_num *= count + 1
	ans.append(div_num)
print('\n'.join(str(i) for i in ans))
