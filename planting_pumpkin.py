from move_to_coord import move_to_xy
from multi_drone_fn import multi_drone_fn_with_original_fn
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
		for _ in range(get_world_size() + 1):
			if get_entity_type() in [Entities.Dead_Pumpkin, None]:
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


def multi_drone_pumpkin_farming(target_amount):		
	multi_drone_fn_with_original_fn(partial(plant_pumpkin_loop, target_amount), partial(pumpkin_merge_check, target_amount), North)