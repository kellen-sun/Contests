flat_num = int(input())
flats = input()
types = set(flats)
shortest_interval = float('inf')
closest_left = 0
curr_caught = {}
for right, f in enumerate(flats):
	if f not in curr_caught:
		curr_caught[f] = 0
	curr_caught[f] += 1
	while closest_left + 1 <= right and curr_caught.get(flats[closest_left], 0) > 1:
		curr_caught[flats[closest_left]] -= 1
		closest_left += 1
	if len(curr_caught) == len(types):
		shortest_interval = min(shortest_interval, right - closest_left + 1)
print(shortest_interval)
