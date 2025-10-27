for i in range(296):
	visited = set()
	if find_treasure(visited, [North, South, East, West]):
		print(i)
	else:
		print("Oh no")
		
for i in range(209):
		if treasure_loop(i):
			continue
		else:
			pass