from f1 import bubble_sort_horizontal, bubble_sort_vertical
from targeted_move import move_to_xy
from multi_drone_util import multi_drone_await_fn

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
