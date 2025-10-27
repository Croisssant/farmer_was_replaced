from targeted_move import move_to, move_to_xy


def bubble_sort(plane, measure_direction):
	original_pos = get_pos_x()
	if plane == "y":
		original_pos = get_pos_y()
	unsorted_list_length = get_world_size()
	
	for i in range(unsorted_list_length):
		swapped = False
		for j in range(unsorted_list_length - i - 1):
			
			if measure() > measure(measure_direction):
				swap(measure_direction)
				swapped = True
				 
			move(measure_direction)
		# RESET POSITION
		
		if plane == "x":
			move_to(original_pos, "x")
		else:
			move_to(original_pos, "y")
			
		if swapped == False:
			if plane == "x":
				move_to(original_pos, "x")
			else:
				move_to(original_pos, "y")
			break


if __name__ == "__main__": 
	move_to_xy(0, 0)
	
	for _ in range(get_world_size()):
		bubble_sort("x", East)
		move(North)
	
	
	for _ in range(get_world_size()):
		bubble_sort("y", North)
		move(East)