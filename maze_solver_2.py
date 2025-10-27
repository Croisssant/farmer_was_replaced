from MazeUtil2 import wall_follow_left, wall_follow_right, create_maze, turn_right, turn_left

def wall_follow_right_and_spawn():
	change_hat(Hats.Golden_Tree_Hat)
	dir = North
	while True:
		m = measure()
		if m == None:
			while measure() == None:
				return 1
				
		right = turn_right(dir)
		left = turn_left(dir)
		
		
		
		if can_move(right):
			dir = right
			
			if can_move(left) and can_move(right) and num_drones() != max_drones():
				spawn_drone(wall_follow_left)
				
			move(dir)
			
		elif can_move(dir):
			move(dir)
		else:
			dir = turn_left(dir)
		
		if get_entity_type() == Entities.Treasure:
			harvest()
			return 1
			
if __name__ == "__main__":
	
	while True:
		if create_maze():
			if wall_follow_right_and_spawn():
				continue
	
	