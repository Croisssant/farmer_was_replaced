from MazeUtil2 import create_maze, treasure_hunt

times = 30

#for i in range(times):
	
	#create_maze()
	#treasure_hunt()

while True:
	if create_maze():
		if treasure_hunt():
			continue