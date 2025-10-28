from move_to_coord import limited_move_to

def initial_apple_search(next_x, next_y):
	EDGE = get_world_size() - 1
	
	for i in range(EDGE):
		limited_move_to(next_y, "y")
		limited_move_to(next_x, "x")
		
		# Recheck the apple's logic
		if get_entity_type() == Entities.Apple:
			next_x, next_y = measure()
		
		curr_y = get_pos_y()
		if  curr_y == next_y:
			if get_world_size() - curr_y > 2:
				move(North)
				move(North)
			else:
				move(South)
				move(South)
			
		
		if i % 2 == 0:
			limited_move_to(EDGE, "x")
		else:
			limited_move_to(0, "x")
	
	if get_pos_x() == 0:
		limited_move_to(4, "y")
		limited_move_to(EDGE, "x")
		limited_move_to(0, "y")
		limited_move_to(0, "x")
	else:
		limited_move_to(0, "y")
		limited_move_to(0, "x")

if __name__ == "__main__":
	initial_apple_search(18, 20)