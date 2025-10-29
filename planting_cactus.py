from farm_traversal import traverse_plot_with_fn
from move_to_coord import move_to, move_to_xy
from utils import should_till, partial
from multi_drone_fn import multi_drone_await_fn, multi_drone_planting

def reset_position(original_pos, plane):
	if plane == "x":
		move_to(original_pos, "x")
	else:
		move_to(original_pos, "y")


def bubble_sort(plane, measure_direction):
	original_pos = get_pos_x()
	if plane == "y":
		original_pos = get_pos_y()
	unsorted_list_length = get_world_size()
	
	for i in range(unsorted_list_length):
		swapped = False
		for _ in range(unsorted_list_length - i - 1):
			
			if measure() > measure(measure_direction):
				swap(measure_direction)
				swapped = True
				 
			move(measure_direction)
		
		# RESET POSITION
		reset_position(original_pos, plane)
			
		if swapped == False:
			reset_position(original_pos, plane)
			break


def sort_cactus_field():
	move_to_xy(0, 0)
	
	for _ in range(get_world_size()):
		bubble_sort("x", East)
		move(North)
	
	
	for _ in range(get_world_size()):
		bubble_sort("y", North)
		move(East)


def plant_cactus():
	curr_plant = Entities.Cactus
	should_till(curr_plant)
	plant(curr_plant)


def plant_cactus_field():
	traverse_plot_with_fn(plant_cactus)


def farming_cactus_loop(target_amount):
	while num_items(Items.Cactus) < target_amount:
		move_to_xy(0, 0)
		plant_cactus_field()
		sort_cactus_field()
		harvest()


def multi_drone_farming_cactus():
	multi_drone_await_fn(partial(multi_drone_planting, Entities.Cactus, East), North)
	multi_drone_await_fn(partial(bubble_sort, "x", East), North)
	move_to_xy(0, 0)
	multi_drone_await_fn(partial(bubble_sort, "y", North), East)
	move_to_xy(0, 0)
	harvest()


def multi_drone_cactus_farming_loop(target_amount):
	while num_items(Items.Cactus) < target_amount:
		multi_drone_farming_cactus()


if __name__ == "__main__": 
	sort_cactus_field()