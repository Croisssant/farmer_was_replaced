from targeted_move import move_to_xy
from multi_drone_util import multi_drone_fn, multi_drone_await_fn

def plant_pumpkin_loop():

	while True:
		if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
			plant(Entities.Pumpkin) 
		move(East)
		
def plant_pumpkin():
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		move(East)
		
def multi_drone(fn, original_drone_fn, move_direction):
	for _ in range(get_world_size() - 1):
		drone = spawn_drone(fn)
		move(move_direction)
		
	original_drone_fn()	

def water_10_times():
	for _ in range(get_world_size() * 10):
		use_item(Items.Water)
		move(East)
		
def plant_healthy_pumpkins():
	while True:
		all_healthy = True
		
		for _ in range(get_world_size()):
			#if get_entity_type() in [Entities.Dead_Pumpkin, None]:
			#if (get_entity_type() == Entities.Dead_Pumpkin and can_harvest()) or get_entity_type() == None:
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

def pumpkin_merge_check():
	while True:
		# Ensure all pumpkins in the row are healthy
		plant_healthy_pumpkins()

		# Check if the row is merged
		while True:
			if check_row_merge():
				harvest()
				break
		
# set_world_size(22)
multi_drone_await_fn(plant_pumpkin, North)
#multi_drone_await_fn(water_10_times, North)
multi_drone(plant_pumpkin_loop, pumpkin_merge_check, North)