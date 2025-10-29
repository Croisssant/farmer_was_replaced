from utils import should_till, should_harvest

def multi_drone_await_fn(fn, move_direction):
	active_drones = []
	for _ in range(min(get_world_size(), max_drones())):
		drone = spawn_drone(fn)
		
		if not drone:
			fn()
			
		else:
			active_drones.append(drone)
		move(move_direction)
			
	for drone in active_drones:
		wait_for(drone)


def multi_drone_fn(fn, move_direction):
	for _ in range(min(get_world_size(), max_drones())):
		drone = spawn_drone(fn)
		if not drone:
			fn()	
			
		move(move_direction)


def multi_drone_fn_with_original_fn(fn, original_drone_fn, move_direction):
	for _ in range(min(get_world_size(), max_drones()) - 1):
		spawn_drone(fn)
		move(move_direction)
		
	original_drone_fn()	


def multi_drone_fn_split(fn_1, fn_2, move_direction):

	for _ in range(min(get_world_size(), max_drones())):
		drone_1 = spawn_drone(fn_1)
		drone_2 = spawn_drone(fn_2)
		
		if not drone_2:
			fn_2()
		if not drone_1:
			fn_1()
			
		move(move_direction)
		move(move_direction)


def multi_drone_planting(curr_plant, move_direction):
	for _ in range(min(get_world_size(), max_drones())):
		should_harvest()
		should_till(curr_plant)
		plant(curr_plant)
		move(move_direction)