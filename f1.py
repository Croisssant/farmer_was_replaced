from targeted_move import move_to, move_to_xy


def bubble_sort_horizontal():
	original_pos = get_pos_x()
	unsorted_list_length = get_world_size()
	
	for i in range(unsorted_list_length):
		swapped = False
		for j in range(unsorted_list_length - i - 1):
			
			if measure() > measure(East):
				swap(East)
				swapped = True
				 
			move(East)
		
		
		move_to(original_pos, "x")
			
		if swapped == False:
			move_to(original_pos, "x")
			break
			
def bubble_sort_vertical():
	original_pos = get_pos_y()
	unsorted_list_length = get_world_size()
	
	for i in range(unsorted_list_length):
		swapped = False
		for j in range(unsorted_list_length - i - 1):
			
			if measure() > measure(North):
				swap(North)
				swapped = True
				 
			move(North)
		
		
		move_to(original_pos, "y")
			
		if swapped == False:
			move_to(original_pos, "y")
			break
			
			