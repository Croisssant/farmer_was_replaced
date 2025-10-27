def shuffle(lst):
	# Fisher–Yates shuffle algorithm
	n = len(lst)
	for i in range(n - 1, 0, -1):
		# pick a random index from 0 to i (inclusive)
		j = random() * (i + 1)
		# swap elements
		lst[i], lst[j] = lst[j], lst[i]
	return lst
		
print(shuffle([North, South, East, West]))