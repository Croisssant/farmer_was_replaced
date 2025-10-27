from initial_apple_search import initial_apple_search
from farm_traversal import traverse_plot_with_fn
from s_walk import s_walk_loop, traverse_plant_and_harvest_sunflower
from targeted_move import move_to_xy

init_x, init_y = (None, None)
def get_first_apple_coords():
	for i in range(get_world_size()):	
		if i % 2 == 0:
			for i in range(get_world_size()):
				if get_entity_type() == Entities.Apple:
					init_x, init_y = measure()
					return (init_x, init_y)
				
				if i == (get_world_size() - 1):
					move(East)
				else:
					move(North)
		else:
			for i in range(get_world_size()):
				if get_entity_type() == Entities.Apple:
					init_x, init_y = measure()
					return (init_x, init_y)
				
				if i == (get_world_size() - 1):
					move(East)
				else:
					move(South)
		

while True:
	#set_world_size(22)
	change_hat(Hats.Sunflower_Hat)
	move_to_xy(0, 0)
	# traverse_plant_and_harvest_sunflower()
	
	change_hat(Hats.Dinosaur_Hat)
	init_x, init_y = get_first_apple_coords()
	initial_apple_search(init_x, init_y)
	s_walk_loop()
