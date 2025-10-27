from targeted_move import move_to_xy
from multi_drone_util import multi_drone_await_fn

def plant_bush():
	if can_harvest():
		harvest()
	plant(Entities.Bush)
		
move_to_xy(0, 0)
multi_drone_await_fn(plant_bush, North)
move_to_xy(0, 0)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)