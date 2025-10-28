def repeated_move(direction, times):
	for _ in range(times):
		move(direction)


def move_to(to_position, plane):
	curr_position = 0
	left = West
	right = East
	
	if plane == "x":
		curr_position = get_pos_x() 
	else:
		curr_position = get_pos_y()
		left = South
		right = North

	diff = to_position - curr_position
	
	if abs(diff) > get_world_size() // 2:
		if diff < 0:
			repeated_move(right, get_world_size() - curr_position + to_position)
	
		else:
			repeated_move(left, get_world_size() + curr_position - to_position)
	
	else:
		if diff < 0:
			repeated_move(left, abs(diff))
			
		else:
			repeated_move(right, diff)
			
		
def limited_move_to(to_position, plane):
	curr_position = 0
	left = West
	right = East
	
	if plane == "x":
		curr_position = get_pos_x() 
	else:
		curr_position = get_pos_y()
		left = South
		right = North

	diff = to_position - curr_position
	
	if diff < 0:
		repeated_move(left, abs(diff))
		
	else:
		repeated_move(right, diff)
		
			
def move_to_xy(to_x, to_y):
	move_to(to_x, "x")
	move_to(to_y, "y")