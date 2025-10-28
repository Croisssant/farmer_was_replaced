from move_to_coord import limited_move_to, move_to_xy
from farm_traversal import traverse_plot_with_fn

def plant_sunflower():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)

def traverse_plant_and_harvest_sunflower():
	traverse_plot_with_fn(plant_sunflower)
	traverse_plot_with_fn(harvest)
	
def s_walk_loop():
	edge_minus_one = get_world_size() - 2
	edge = get_world_size() - 1
	
	while True:
		for _ in range(15):
			move(North)
			limited_move_to(edge_minus_one, "x")
			move(North)
			limited_move_to(0, "x")
		if move(North):
			limited_move_to(edge, "x")
			limited_move_to(0, "y")
			limited_move_to(0, "x")
		else:
			break

if __name__ == "__main__": 
	edge_minus_one = get_world_size() - 2
	edge = get_world_size() - 1
	move_to_xy(0, 0)
	change_hat(Hats.Sunflower_Hat)
	traverse_plot_with_fn(plant_sunflower)
	traverse_plot_with_fn(harvest)
	change_hat(Hats.Dinosaur_Hat)
	
	while True:
		for _ in range(10):
			move(North)
			limited_move_to(edge_minus_one, "x")
			move(North)
			limited_move_to(0, "x")
		if move(North):
			limited_move_to(edge, "x")
			limited_move_to(0, "y")
			limited_move_to(0, "x")
		else:
			change_hat(Hats.Sunflower_Hat)
			move_to_xy(0, 0)
			 
			traverse_plot_with_fn(plant_sunflower)
			traverse_plot_with_fn(harvest)
			change_hat(Hats.Dinosaur_Hat)
			
			# break

