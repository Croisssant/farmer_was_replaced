from multi_drone_util import multi_drone_await_fn, multi_drone_fn_split

		
def keep_moving_east():
	while True:
		if can_harvest():
			harvest()
		move(East)

def keep_moving_west():
	while True:
		if can_harvest():
			harvest()
		move(West)
		
def water_10_times():
	for _ in range(160):
		use_item(Items.Water)
		move(East)


def plant_carrot_loop_east():
	while True:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		move(East)
		
def plant_carrot_loop_west():
	while True:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		move(West)

def plant_carrots():
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		move(East)
		
set_world_size(16)
multi_drone_await_fn(plant_carrots, North)
multi_drone_await_fn(water_10_times, North)
multi_drone_fn_split(plant_carrot_loop_east, plant_carrot_loop_west, North)