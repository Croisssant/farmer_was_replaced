from move_to_coord import move_to, move_to_xy
from multi_drone_util import multi_drone_await_fn

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
			

def plant_cactus():
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		move(East)


while True:
	multi_drone_await_fn(plant_cactus, North)
	multi_drone_await_fn(bubble_sort_horizontal, North)
	move_to_xy(0, 0)
	multi_drone_await_fn(bubble_sort_vertical, East)
	move_to_xy(0, 0)
	harvest()
