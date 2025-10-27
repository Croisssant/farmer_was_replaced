from multi_drone_util import multi_drone_await_fn, multi_drone_fn
from targeted_move import move_to_xy	
def keep_moving():
	while True:
		move(East)


def plant_sunflower_loop():
	while get_water() > 0.5:
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		move(East)


def harvest_loop():
	while True:
		if can_harvest():
			harvest()
		move(East)

def plant_carrot_loop():
	while True:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		move(East)
		
def plant_carrot():
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		move(East)


def farm_weird_substance_loop():
	while True:
		if can_harvest():
			harvest()
			use_item(Items.Fertilizer)
		move(East)
		
		
def water_10_times():
	for _ in range(get_world_size() * 5):
		use_item(Items.Water)
		move(East)
		

if __name__ == "__main__":			
	# multi_drone_fn(plant_carrot, North)
	while True:
		move_to_xy(0, 0)
		#multi_drone_await_fn(water_10_times, North)
		multi_drone_await_fn(farm_weird_substance_loop, North)