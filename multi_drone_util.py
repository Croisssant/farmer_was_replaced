from utils import should_till, should_harvest, partial

def multi_drone_await_fn(fn, move_direction):
	active_drones = []
	for _ in range(get_world_size()):
		drone = spawn_drone(fn)
		
		if not drone:
			fn()
			
		else:
			active_drones.append(drone)
		move(move_direction)
			
	for drone in active_drones:
		wait_for(drone)


def multi_drone_fn(fn, move_direction):
	for _ in range(get_world_size()):
		drone = spawn_drone(fn)
		if not drone:
			fn()	
			
		move(move_direction)


def multi_drone_fn_split(fn_1, fn_2, move_direction):

	for _ in range(get_world_size()):
		drone_1 = spawn_drone(fn_1)
		drone_2 = spawn_drone(fn_2)
		
		if not drone_2:
			fn_2()
		if not drone_1:
			fn_1()
			
		move(move_direction)


def multi_drone_planting(curr_plant, move_direction):
	for _ in range(get_world_size()):
		should_harvest()
		should_till(curr_plant)
		plant(curr_plant)
		move(move_direction)