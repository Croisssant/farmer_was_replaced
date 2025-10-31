from farm_traversal import traverse_plot_with_fn
from move_to_coord import move_to_xy
from multi_drone_fn import multi_drone_await_fn, multi_drone_fn_with_original_fn
from planting_helpers import check_harvest_plant
from utils import partial

def plant_pumpkin_loop(target_amount):
	while num_items(Items.Pumpkin) < target_amount:
		if get_entity_type() in [Entities.Dead_Pumpkin, None]:
			plant(Entities.Pumpkin) 
		move(East)
		

def plant_healthy_pumpkins():
	while True:
		all_healthy = True
		
		# Do an additional check for just planted pumpkins (where it is missed sometimes)
		# The current bug is that the check still continues while just planted pumpkins
		# are still growing, hence they're missed during the checks. 
		# Current solution now is just to check the row 4 times, where it's about the same time as allowing
		# the just planted pumpkins to grow.
		# Future improved solution, await for just planted pumpkin before the next check?
		for _ in range(get_world_size()):
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
				all_healthy= False
				
			move(East)
		
		if all_healthy:
			break
		

def check_row_merge():
	move_to_xy(0, 0)
	bottom_left_id = measure()
	move_to_xy(get_world_size() - 1, get_world_size() - 1)
	top_right_id = measure()
	
	if bottom_left_id == top_right_id:
		return True
	return False


def pumpkin_merge_check(target_amount):
	while num_items(Items.Pumpkin) < target_amount:
		# Ensure all pumpkins in the row are healthy
		plant_healthy_pumpkins()

		# Check if the row is merged
		while True:
			if check_row_merge():
				harvest()
				break
			else:
				plant_healthy_pumpkins()

def plant_pumpkin():
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		move(East)


def multi_drone_pumpkin_farming(target_amount):
	multi_drone_await_fn(plant_pumpkin, North)
	multi_drone_fn_with_original_fn(partial(plant_pumpkin_loop, target_amount), partial(pumpkin_merge_check, target_amount), North)


def replace_bad_pumpkins():
	if get_entity_type() in [Entities.Dead_Pumpkin, None]:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin) 

def just_plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)

def single_drone_pumpkin_farming(target_amount, resource):
	while num_items(resource) < target_amount:
		traverse_plot_with_fn(just_plant_pumpkin)
		move_to_xy(0, 0)
		bottom_left_id = measure()
		move_to_xy(get_world_size() - 1, get_world_size() - 1)
		top_right_id = measure()

		while bottom_left_id != top_right_id:
			traverse_plot_with_fn(replace_bad_pumpkins)
			move_to_xy(0, 0)
			bottom_left_id = measure()
			move_to_xy(get_world_size() - 1, get_world_size() - 1)
			top_right_id = measure()

		harvest()


def pumpkin_farming():
	traverse_plot_with_fn(just_plant_pumpkin)
	move_to_xy(0, 0)
	bottom_left_id = measure()
	move_to_xy(get_world_size() - 1, get_world_size() - 1)
	top_right_id = measure()

	while bottom_left_id != top_right_id:
		traverse_plot_with_fn(replace_bad_pumpkins)
		move_to_xy(0, 0)
		bottom_left_id = measure()
		move_to_xy(get_world_size() - 1, get_world_size() - 1)
		top_right_id = measure()

	harvest()